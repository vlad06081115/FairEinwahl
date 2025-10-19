import logging
from . import config
import pandas as pd
from .pref_to_sport import preferences_to_sports
from ortools.linear_solver import pywraplp

logger = logging.getLogger(__name__)


def norm(s : str) -> str:
    if not isinstance(s, str):
        return ''
    
    if ':' in s:
        return s.split(':')[0].lower().strip()
    
    return s.lower().strip()


def students_appointing(df : pd.DataFrame, programms : dict) -> dict:
    # dict with dataframes for every semestr
    semestrs_dataframes = {}

    def fill_in_semestrs_dataframe(programms : dict) -> None:
        for part, sports in programms.items():
            semestrs_dataframes[part] = pd.DataFrame(columns=sports)

    fill_in_semestrs_dataframe(programms= programms)

    data = df.to_numpy()

    nachname_idx = df.columns.get_loc('Nachname')
    vorname_idx = df.columns.get_loc('Vorname')

    m1, m2, m3 = df.columns.get_loc('M-Präferenz 1'), df.columns.get_loc('M-Präferenz 2'), df.columns.get_loc('M-Präferenz 3')
    i1, i2, i3 = df.columns.get_loc('I-Präferenz 1'), df.columns.get_loc('I-Präferenz 2'), df.columns.get_loc('I-Präferenz 3')

    solver = pywraplp.Solver.CreateSolver('SCIP')

    pref_sport = {}
    
    x = {}
    for row_idx, i in enumerate(data):
        for s in programms.keys():
            for c in programms[s]:
                x[row_idx, s, c] = solver.IntVar(0, 1, f"x_{row_idx}_{s}_{c}")
        
        pref_sport[row_idx] = {
            'm_pref' : preferences_to_sports([data[row_idx][m1], data[row_idx][m2], data[row_idx][m3]]),
            'i_pref' : preferences_to_sports([data[row_idx][i1], data[row_idx][i2], data[row_idx][i3]])
        }
    
    for row_idx, i in enumerate(data):
        for s in programms.keys():
            solver.Add(sum(x[row_idx, s, c] for c in programms[s]) == 1)
            

    for s in programms.keys():
        for c in programms[s]:
            solver.Add(sum(x[row_idx, s, c] for row_idx, i in enumerate(data)) >= config.MIN_CAPACITY)
            solver.Add(sum(x[row_idx, s, c] for row_idx, i in enumerate(data)) <= config.MAX_CAPACITY)
    
    stat = {}      
    objective = solver.Objective()
    for row_idx, i in enumerate(data):
        for s in programms.keys():
            for c in programms[s]:
                
                m_preferences = pref_sport[row_idx]['m_pref']
                i_preferences = pref_sport[row_idx]['i_pref']

                score = 0
                
                if c in m_preferences:
                    score =  3 - m_preferences.index(c)

                elif c in i_preferences:
                    score = 3 - i_preferences.index(c)
                
                else: 
                    pass

                stat[(row_idx, s, c)] = round(score / config.MAX_SEMESTR_SATISFACTION * 100, 2)
                objective.SetCoefficient(x[row_idx, s, c], score)

    objective.SetMaximization()
    
    status = solver.Solve()
    
    statistik_df = pd.DataFrame(columns= ['semestr', 'student', 'sport', 'sat'])
    
    if status == pywraplp.Solver.OPTIMAL:
        for row_idx, i in enumerate(data):
            for s in programms.keys():
                for c in programms[s]:    
                    if x[row_idx, s, c].solution_value() > 0.5:
                        
                        semestrs_dataframes[s].loc[
                            semestrs_dataframes[s][c].notna().sum(), c
                        ] = f"{norm(data[row_idx][nachname_idx])} {norm(data[row_idx][vorname_idx])}"
                        
                        sat = stat[(row_idx, s, c)]
                        statistik_df.loc[len(statistik_df)] = [s, f"{norm(data[row_idx][nachname_idx])} {norm(data[row_idx][vorname_idx])}", c, sat]
        
        logger.debug(statistik_df)
        logger.info(f"Succesfully appointed students!")
        
        for sem, table in semestrs_dataframes.items():
            logger.debug(f"Table for {sem}:\n{table}")
        
    else:
        logger.warning(f"Something went wrong!")
    
    return semestrs_dataframes, statistik_df
    
