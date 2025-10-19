import logging
import pandas as pd
from Modules import config
from Modules import configure_logging
from Modules import semestr_programms_forming
from Modules import building_model
from Modules import schedule_to_PROGRAMMS
from Modules import students_appointing
from Modules import statistik_count
from Modules import df_toExel
from Modules import stat_to_pdf

configure_logging()

logger = logging.getLogger(__name__)

df = pd.read_excel(config.INPUT_FILE, skiprows=1, usecols="A:N")


def main(df: pd.DataFrame):

    groups, sport_fest = semestr_programms_forming(df)

    schedule = building_model(
        required_groups=groups,
        sport_fest=sport_fest,
        semestrs=config.SEMESTRS,
        slots=config.SLOTS,
    )

    programms = schedule_to_PROGRAMMS(schedule=schedule)

    semestrs_dataframes, statistik_df = students_appointing(df=df, programms=programms)

    for semestr in semestrs_dataframes:
        logger.info(
            f"{semestr} \n{semestrs_dataframes[semestr].notna().sum()} \n{semestrs_dataframes[semestr]}"
        )

    df_toExel(df=semestrs_dataframes)

    statistik_summary = statistik_count(statistik_df)
    
    stat_to_pdf(statistik_summary= statistik_summary, semestrs_dfs= semestrs_dataframes)


main(df)
