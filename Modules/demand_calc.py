import logging
import math
from collections import Counter
from .pref_to_sport import preferences_to_sports
from . import config

logger = logging.getLogger(__name__)


def semestr_programms_forming(df):

    sport_fest = False

    def compute_demand(student):

        WEIGHTS = (3, 2, 1)

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

        count_anywhere = Counter()
        weighted_count = Counter()

        for pos, sport in enumerate(m_preferences):
            weighted_count[sport] += WEIGHTS[pos]
            count_anywhere[sport] += 1

        for pos, sport in enumerate(i_preferences):
            weighted_count[sport] += WEIGHTS[pos]
            count_anywhere[sport] += 1

        return count_anywhere, weighted_count

    def maximum_groups_check(groups: dict, amount_groups: int, effective_students: int):

        overcrowded_points = int(amount_groups - 9)

        for i in range(overcrowded_points):

            suitable_sports = [sport for sport, value in groups.items() if value > 1]

            sport_loads_delta = {}
            for sport in suitable_sports:

                load_now = effective_students[sport] / groups[sport]

                load_after = effective_students[sport] / (groups[sport] - 1)

                delta = load_after - load_now

                sport_loads_delta[sport] = delta

            logger.debug(f"sport load - {sport_loads_delta}")

            min_sport = min(sport_loads_delta, key=sport_loads_delta.get)
            logger.debug(f"min_sport : {min_sport}")

            groups[min_sport] -= 1

        logger.debug(f"sum(groups.values()) : {sum(groups.values())}")
        return groups

    result_demand = df.apply(lambda row: compute_demand(row), axis="columns")

    def get_required_groups(result_demand):
        count_anywhere = [res[0] for res in result_demand]
        weighted_count = [res[1] for res in result_demand]

        total_count_anywhere = sum(count_anywhere, Counter())
        total_weighted_count = sum(weighted_count, Counter())

        mean_weight = sum(total_weighted_count.values()) / sum(
            total_count_anywhere.values()
        )

        effective_students = {}
        for sport in total_weighted_count.keys():
            effective_students[sport] = total_weighted_count[sport] / mean_weight

        required_groups = {}
        ceil_values = {}
        total_floor = 0

        for sport, eff in effective_students.items():
            floor_val = int(eff // config.MAX_CAPACITY)
            ceil_val = math.ceil(eff / config.MAX_CAPACITY)
            required_groups[sport] = floor_val
            ceil_values[sport] = ceil_val
            total_floor += floor_val
            logger.debug(f"{sport}: eff={eff:.2f}, floor={floor_val}, ceil={ceil_val}")

        if total_floor < 9:
            logger.warning("Total floor groups < 9 — использую ceil values")
            required_groups = ceil_values.copy()

        logger.debug(f"Mean weight : , {mean_weight}")
        logger.debug(f"Anywhere count:, {total_count_anywhere}")
        logger.debug(f"Weighted count:, {total_weighted_count}")
        logger.debug(f"Effective students:, {effective_students}")
        logger.debug(f"Required groups:, {required_groups}")
        logger.debug(f"sports in required groups - {sum(required_groups.values())}")

        return required_groups, total_count_anywhere, effective_students

    required_groups, total_count_anywhere, effective_students = get_required_groups(
        result_demand=result_demand
    )

    logger.info(
        f"Final required_groups={required_groups}, total={sum(required_groups.values())}"
    )

    if total_count_anywhere[config.FIXED_SPORT] >= config.MIN_CAPACITY:
        required_groups[config.FIXED_SPORT] = 1
        sport_fest = True

    amount_groups = sum(required_groups.values())

    groups = required_groups.copy()
    if amount_groups > config.TOTAL_GROUPS:
        groups = maximum_groups_check(
            groups=required_groups,
            amount_groups=amount_groups,
            effective_students=effective_students,
        )

    return groups, sport_fest
