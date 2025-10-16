import pandas as pd
import logging
from . import preferences_to_sports
from . import config
from collections import defaultdict

logger = logging.getLogger(__name__)


def norm(s: str):
    if not isinstance(s, str):
        return ""

    return str(s).split(":")[0].lower().strip()


def cell_contains_student(student, val):

    if pd.isna(val):
        return False

    student_vorname = norm(student.Vorname)
    student_nachname = norm(student.Nachname)

    vor_nach = " ".join([student_vorname, student_nachname])
    nach_vor = " ".join([student_nachname, student_vorname])

    return norm(val) in {vor_nach, nach_vor}


def statistik_count(all_formed_semestrs_df: dict, basik_df: pd.DataFrame):

    data = {"student": []}

    for semestr in all_formed_semestrs_df:
        data[f"{semestr}_satisfaction"] = []

    data["total_satisfaction"] = []

    personal_statistik_df = pd.DataFrame(data)

    students_in_semestrs = {}

    
    def get_students_in_semestrs(student):

        student_data = {}

        for semestr in all_formed_semestrs_df:
            student_data.setdefault(semestr, "")

        for semestr, df in all_formed_semestrs_df.items():

            for sport in df.columns:

                values = df[sport].dropna().tolist()

                if any(
                    cell_contains_student(student=student, val=val) for val in values
                ):

                    student_data[semestr] = sport

        student_name = " ".join([norm(student.Nachname), norm(student.Vorname)])

        students_in_semestrs[student_name] = student_data

    def personal_statistik_count(student):

        student_name = " ".join([norm(student.Nachname), norm(student.Vorname)])
        
        sports = list(students_in_semestrs[student_name].values())
        if all(s == "" for s in sports):
            logger.warning(f"{student_name} не найден ни в одном семестре!\n{sports}")
            
            return
        
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

        pers_statistik_summary = []
        pers_statistik_summary.append(
            " ".join([norm(student.Nachname), norm(student.Vorname)])
        )  # adding name to statistik

        student_name = " ".join([norm(student.Nachname), norm(student.Vorname)])

        sum_semestrs_satisfaction = 0
        for semestr, sport in students_in_semestrs[student_name].items():

            semestr_satisfaction = 0

            if sport in m_preferences:
                semestr_satisfaction = 3 - m_preferences.index(sport)
            elif sport in i_preferences:
                semestr_satisfaction = 3 - i_preferences.index(sport)

            pers_statistik_summary.append(
                round(semestr_satisfaction / config.MAX_SEMESTR_SATISFACTION, 2) * 100
            )
            sum_semestrs_satisfaction += semestr_satisfaction

        pers_statistik_summary.append(
            round(sum_semestrs_satisfaction / config.MAX_TOTAL_SATISFACTION, 2) * 100
        )
        personal_statistik_df.loc[len(personal_statistik_df)] = pers_statistik_summary

    def sports_statistik(students_semestrs):
        rowSemestr_colStudent_sports = pd.DataFrame(students_semestrs)

        sports_satisfaction = {}
        for sport in config.SPORTS.values():

            current_sport_satisfaction = 0
            count = 0

            for semestr in rowSemestr_colStudent_sports.index:

                semestr_student_sport = rowSemestr_colStudent_sports.loc[semestr]
                students_with_sport = semestr_student_sport.loc[
                    semestr_student_sport == sport
                ].index.to_list()

                if students_with_sport:
                    mean = personal_statistik_df.loc[
                        personal_statistik_df["student"].isin(students_with_sport)
                    ][f"{semestr}_satisfaction"].mean()
                    logger.info(
                        f"semestr --> {semestr}\nsport --> {sport}\n{students_with_sport}\nlen --> {len(students_with_sport)}\nmean satisfaction - {mean}"
                    )
                    current_sport_satisfaction += mean
                    count += 1

            if count:
                sports_satisfaction[sport] = float(
                    round(current_sport_satisfaction / count, 2)
                )

        sports_satisfaction = dict(
            sorted(sports_satisfaction.items(), key=lambda x: x[1], reverse=True)
        )
        sports_satisfaction = pd.DataFrame.from_dict(
            data=sports_satisfaction, orient="index", columns=["mean_satisfaction"]
        )
    
        return sports_satisfaction

    def get_semestrs_statistik():

        semestrs_statistik = {}
        for semestr in config.SEMESTRS:

            current_semestr = f"{semestr}_satisfaction"
            current_semestr_satisfaction = personal_statistik_df[current_semestr]

            semestrs_statistik[semestr] = float(
                round(current_semestr_satisfaction.mean(), 2)
            )

        semestrs_statistik = pd.DataFrame.from_dict(
            data=semestrs_statistik, orient="index", columns=["mean_satisfaction"]
        )

        return semestrs_statistik

    def satisfaction_distribution():

        bins = [0, 30, 60, 85, 100]
        labels = config.SATISFACTION_DISTRIBUTION

        categories = pd.cut(
            personal_statistik_df["total_satisfaction"], bins=bins, labels=labels
        )

        distribution = categories.value_counts()

        return distribution

    def statistik_summary():
        mean_satisfaction = round(personal_statistik_df["total_satisfaction"].mean(), 2)
        min_satisfaction = round(personal_statistik_df["total_satisfaction"].min(), 2)
        max_satisfaction = round(personal_statistik_df["total_satisfaction"].max(), 2)

        std_sat = round(personal_statistik_df["total_satisfaction"].std(), 2)
        var_sat = round(personal_statistik_df["total_satisfaction"].var(), 2)

        median = round(personal_statistik_df["total_satisfaction"].median(), 2)

        sports_mean_satisfaction = sports_statistik(
            students_semestrs=students_in_semestrs
        )

        semestrs_mean_satisfaction = get_semestrs_statistik()

        sat_distribution = satisfaction_distribution()

        solo_stat = {
            'mean satisfaction' : mean_satisfaction,
            'min satisfaction' : min_satisfaction,
            'max satisfaction' : max_satisfaction,
            'standard deviation' : std_sat,
            'dispercion' : var_sat,
            'median satisfaction' : median
        }
        
        stat_summary = {
            'solo_stat' : solo_stat,
            'sports_satisfaction' : sports_mean_satisfaction,
            'semestrs_satisfaction' : semestrs_mean_satisfaction,
            'satisfaction_distribution' : sat_distribution
        }
        
        return stat_summary
        
    basik_df.apply(lambda student: get_students_in_semestrs(student), axis="columns")
    logger.debug(f"{students_in_semestrs}")

    basik_df.apply(lambda student: personal_statistik_count(student), axis="columns")
   
    stat_summary = statistik_summary()
    
    stat_summary['personal'] = personal_statistik_df
    
    #logging all statistiks
    for stat_name, stat in stat_summary.items():
        
        logger.info(
            f"statistiks of {stat_name} :\n{round(stat, 2) if isinstance(stat, (int, float)) else stat}"
        )
    
    unsat_students = personal_statistik_df.loc[personal_statistik_df['total_satisfaction'] == float(0)]
    
    logger.critical(f"{unsat_students}")
    
    logger.critical([students_in_semestrs[student] for student in unsat_students['student']])
    return stat_summary



# Средняя удовлетворённость по каждому виду спорта
# Средняя удовлетворённость по каждому семестру
# Самый "непопулярный" спорт
# Распределение удовлетворённости
# — например, гистограмма, сколько учеников попадает в диапазоны:
# 0–30%, 30–60%, 60–90%, 90–100%.
# Это можно красиво отобразить в Excel (цветами или графиком).
