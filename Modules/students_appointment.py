import logging
from . import config
import pandas as pd
from .pref_to_sport import preferences_to_sports
# from scipy.optimize import linear_sum_assignment

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

    def fill_in_semestrs_dataframe(programms : dict):
        for part, sports in programms.items():
            semestrs_dataframes[part] = pd.DataFrame(columns=sports)

    fill_in_semestrs_dataframe(programms= programms)

    data = df.to_numpy()

    nachname_idx = df.columns.get_loc('Nachname')
    vorname_idx = df.columns.get_loc('Vorname')

    m1, m2, m3 = df.columns.get_loc('M-Präferenz 1'), df.columns.get_loc('M-Präferenz 2'), df.columns.get_loc('M-Präferenz 3')
    i1, i2, i3 = df.columns.get_loc('I-Präferenz 1'), df.columns.get_loc('I-Präferenz 2'), df.columns.get_loc('I-Präferenz 3')





    for semestr, sports in programms.items():
        
        solver = pywraplp.Solver.CreateSolver('SCIP')

        x = {}
        for i in data:
            for s in sports:
                x[i[nachname_idx], s] = solver.IntVar(0, 1, f"x_{i[nachname_idx]}_{s}")

        for i in data:
            solver.Add(sum(x[i[nachname_idx], s] for s in sports) == 1)
            
        for s in sports:
            solver.Add(sum(x[i[nachname_idx], s] for i in data) >= config.MIN_CAPACITY)
            solver.Add(sum(x[i[nachname_idx], s] for i in data) <= config.MAX_CAPACITY)

        objective = solver.Objective()
        for i in data:
            for s in sports:
                
                m_preferences = preferences_to_sports([i[m1], i[m2], i[m3]])
                i_preferences = preferences_to_sports([i[i1], i[i2], i[i3]])
                
                if s in m_preferences:
                    objective.SetCoefficient(x[i[nachname_idx], s], 3 - m_preferences.index(s))

                elif s in i_preferences:
                    objective.SetCoefficient(x[i[nachname_idx], s], 3 - i_preferences.index(s))

        objective.SetMaximization()

        status = solver.Solve()

        if status == pywraplp.Solver.OPTIMAL:
            for i in data:
                for s in sports:
                    if x[i[nachname_idx], s].solution_value() > 0.5:
                        semestrs_dataframes[semestr].loc[
                            semestrs_dataframes[semestr][s].notna().sum(), s
                        ] = norm(f"{norm(i[nachname_idx])} {norm(i[vorname_idx])}")

    for semestr, schedule in semestrs_dataframes.items():
        
        logger.info(f"{semestr}\n{schedule}")
    
    return semestrs_dataframes
    
