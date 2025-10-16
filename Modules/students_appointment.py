import logging
from . import config
import pandas as pd
from .pref_to_sport import preferences_to_sports
from scipy.optimize import linear_sum_assignment

logger = logging.getLogger(__name__)


def norm(s : str) -> str:
    if not isinstance(s, str):
        return ''
    
    if ':' in s:
        return s.split(':')[0].lower().strip()
    
    return s.lower().strip()


def students_appointing(df, programms):
    # dict with dataframes for every semestr
    semestrs_dataframes = {}

    def fill_in_semestrs_dataframe(programms : dict):
        for part, sports in programms.items():
            semestrs_dataframes[part] = pd.DataFrame(columns=sports)

    # creating a list of all available sports
    def expanded_sports(sports_list: list):
        expanded_sports_list = []

        for sport in sports_list:
            for i in range(config.MAX_CAPACITY):
                expanded_sports_list.append(f"{sport}_{i+1}")

        return expanded_sports_list

    def u_matrix(student, expanded_sports: list):

        m_preferences = preferences_to_sports(
            [
                student["M-Präferenz 1"],
                student["M-Präferenz 2"],
                student["M-Präferenz 3"],
            ]
        )
        i_preferences = preferences_to_sports(
            [
                student["I-Präferenz 1"],
                student["I-Präferenz 2"],
                student["I-Präferenz 3"],
            ]
        )
        
        row = []
        for sport in expanded_sports:
            sport = sport.split("_")[0]
            if sport in m_preferences:
                score_m = 3 - m_preferences.index(sport)
            if sport in i_preferences:
                score_i = 3 - i_preferences.index(sport)
            if (sport not in m_preferences) and (sport not in i_preferences):
                score = 0
                row.append(score)
                continue

            if (sport in m_preferences) and (sport in i_preferences):
                score = max(score_i, score_m)
            elif sport in m_preferences:
                score = score_m
            elif sport in i_preferences:
                score = score_i
            row.append(score)
        
        return row
    
    

    def check_min_requirment(
        row_col, semestr, U_matrix, expanded_sports_list, C_matrix
    ):
        for sport in semestrs_dataframes[semestr].columns:
            sport_capacity = semestrs_dataframes[semestr][sport].notna().sum()

            if sport_capacity < config.MIN_CAPACITY:

                needed = config.MIN_CAPACITY - sport_capacity

                logger.info(
                    f"{semestr}\n{semestrs_dataframes[semestr].notna().sum()}\n{semestrs_dataframes[semestr]}\nneeded: {needed}"
                )

                candidates = []
                for r, c in row_col:
                    current_sport = expanded_sports_list[c].split("_")[0]

                    if current_sport == sport:
                        continue

                    score_now = U_matrix[r][c]
                    score_sport = U_matrix[r][expanded_sports_list.index(f"{sport}_1")]

                    delta = score_sport - score_now
                    candidates.append(
                        [r, current_sport, score_now, score_sport, delta, c]
                    )

                max_delta = -10
                max_delta_index = []

                for i, row in enumerate(candidates):
                    if row[4] >= max_delta:
                        max_delta = row[4]
                        max_delta_index.append(i)

                for i in range(needed):
                    # add a student to needed sport
                    
                    student = candidates[max_delta_index[-1]][0]
                    score_new = candidates[max_delta_index[-1]][3]

                    semestrs_dataframes[semestr].loc[
                        semestrs_dataframes[semestr][sport].notna().sum(), sport
                    ] = f"{df.iloc[student]['Nachname']} {df.iloc[student]['Vorname']} : {score_new}"

                    # delete student from old sport

                    sport_col = candidates[max_delta_index[-1]][1]
                    student_name = df.iloc[student]["Nachname"]
                    score_old = C_matrix[student][candidates[max_delta_index[-1]][5]]
                    mask = (
                        semestrs_dataframes[semestr][sport_col]
                        != f"{student_name} : {score_old}"
                    )
                    semestrs_dataframes[semestr][sport_col] = semestrs_dataframes[
                        semestr
                    ][sport_col][mask].reset_index(drop=True)

                    candidates.pop(max_delta_index[-1])
                    max_delta_index.pop(-1)
                    

    def main():

        fill_in_semestrs_dataframe(programms)

        for semestr in programms.keys():
            expanded_sports_list = expanded_sports(programms[semestr])
            U = []
            df.apply(
                lambda student: U.append(u_matrix(student, expanded_sports_list)),
                axis="columns",
            )
            
            max_u = max(max(row) for row in U)
            C = [[max_u - val for val in row] for row in U]

            logger.info(f"students: {len(df)}, slots: {len(expanded_sports_list)}")
            logger.info(f"U matrix rows: {len(U)}, U matrix cols: {len(U[0]) if U else 0}")
            
            row_ind, col_ind = linear_sum_assignment(C)
            
            assigned_rows = set(row_ind)
            unassigned = [i for i in range(len(df)) if i not in assigned_rows]
            logger.warning(f"UNASSIGNED STUDENTS COUNT: {len(unassigned)}, list: {unassigned}")
            
            for r, c in zip(row_ind, col_ind):
                sport = expanded_sports_list[c].split("_")[0]
                semestrs_dataframes[semestr].loc[
                    semestrs_dataframes[semestr][sport].notna().sum(), sport
                ] = norm(f"{df.iloc[r]['Nachname']} {df.iloc[r]['Vorname']}")
                
            check_min_requirment(
                row_col=zip(row_ind, col_ind),
                semestr=semestr,
                U_matrix=U,
                expanded_sports_list=expanded_sports_list,
                C_matrix=C,
            )

    main()

    return semestrs_dataframes
