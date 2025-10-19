import pandas as pd
import logging
from . import config


logger = logging.getLogger(__name__)


def statistik_count(statistik_df : pd.DataFrame):

    logger.warning(statistik_df)
    
    sport_mean_sat = round(statistik_df.groupby('sport')['sat'].mean().sort_values(ascending= False), 2)
    
    logger.warning(sport_mean_sat)
    
    semestrs_mean_sat = round(statistik_df.groupby('semestr')['sat'].mean(), 2)
    
    logger.warning(semestrs_mean_sat)
    
    bins = [0, 30, 60, 85, 100]
    labels = config.SATISFACTION_DISTRIBUTION
    
    categories = pd.cut(
        statistik_df.groupby('student')['sat'].mean(), bins= bins, labels= labels
    )
    
    distribution = categories.value_counts()
    logger.info(f"distribution - {distribution}")
    
    mean_sat = round(statistik_df.groupby('student')['sat'].mean().mean(), 2)
    logger.info(f"mean sat - {mean_sat}")
    
    min_sat = round(statistik_df.groupby('student')['sat'].mean().min(), 2)
    logger.info(f"min sat - {min_sat}")
    
    max_sat = round(statistik_df.groupby('student')['sat'].mean().max(), 2)
    logger.info(f"max sat - {max_sat}")
    
    std_sat = round(statistik_df.groupby('student')['sat'].mean().std(), 2)
    logger.info(f"std sat - {std_sat}")
    
    var_sat = round(statistik_df.groupby('student')['sat'].mean().var(), 2)
    logger.info(f"var sat - {var_sat}")
    
    median_sat = round(statistik_df.groupby('student')['sat'].mean().median(), 2)
    logger.info(f"median sat - {median_sat}")
    
    solo_stat = {
        'mean_satisfaction' : mean_sat,
        'min_satisfaction' : min_sat,
        'max_satisfaction' : max_sat,
        'standard_deviation' : std_sat,
        'dispercion' : var_sat,
        'median_satisfaction' : median_sat
    }
    
    stat_summary = {
        'solo_stat' : solo_stat,
        'sports_satisfaction' : sport_mean_sat,
        'semestrs_satisfaction' : semestrs_mean_sat,
        'satisfaction_distribution' : distribution,
        'statistik_df' : statistik_df
    }
    
    return stat_summary
    