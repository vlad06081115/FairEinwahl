from . import config
import pandas as pd


def preferences_to_sports(preferences: list):
    """
    a list of number given and a list of sport converted according
    to config.SPORTS returned
    """

    preferences = [pref for pref in preferences if not pd.isna(pref)]

    for i, pref in enumerate(preferences):

        preferences[i] = config.SPORTS[pref]

    return preferences
