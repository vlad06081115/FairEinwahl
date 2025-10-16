def schedule_to_PROGRAMMS(schedule):
    programms = {}

    for semestr, sports in schedule.items():
        sport_list = []
        for sport in sports.values():
            sport_list.append(sport)

        programms[semestr] = sport_list

    return programms
