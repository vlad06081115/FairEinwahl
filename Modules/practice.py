from ortools.linear_solver import pywraplp
import pandas as pd
import config



def preferences_to_sports(preferences: list):
    """
    a list of number given and a list of sport converted according
    to config.SPORTS returned
    """

    preferences = [pref for pref in preferences if not pd.isna(pref)]

    for i, pref in enumerate(preferences):

        preferences[i] = config.SPORTS[pref]

    return preferences

semestrs_dataframes = {}

def fill_in_semestrs_dataframe(programms : dict):
    for part, sports in programms.items():
        semestrs_dataframes[part] = pd.DataFrame(columns=sports)


df = pd.read_excel(config.INPUT_FILE, skiprows=1, usecols="A:N")

programms = {11.1: ['Leichtathletik', 'Badminton', 'Gymnastik/Tanz'], 
             11.2: ['Fußball', 'Basketball', 'Volleyball'], 
             12.1: ['Volleyball', 'Basketball', 'Badminton']}

fill_in_semestrs_dataframe(programms= programms)

max_cap = config.MAX_CAPACITY
min_cap = config.MIN_CAPACITY

data = df.to_numpy()

nachname_idx = df.columns.get_loc('Nachname')
vorname_idx = df.columns.get_loc('Vorname')

m1, m2, m3 = df.columns.get_loc('M-Präferenz 1'), df.columns.get_loc('M-Präferenz 2'), df.columns.get_loc('M-Präferenz 3')
i1, i2, i3 = df.columns.get_loc('I-Präferenz 1'), df.columns.get_loc('I-Präferenz 2'), df.columns.get_loc('I-Präferenz 3')

solver = pywraplp.Solver.CreateSolver('SCIP')

x = {}
for row_idx, i in enumerate(data):
    for s in programms.keys():
        for c in programms[s]:
            x[row_idx, s, c] = solver.IntVar(0, 1, f"x_{row_idx}_{s}_{c}")

for row_idx, i in enumerate(data):
    for s in programms.keys():
        solver.Add(sum(x[row_idx, s, c] for c in programms[s]) == 1)
        

for s in programms.keys():
    for c in programms[s]:
        solver.Add(sum(x[row_idx, s, c] for row_idx, i in enumerate(data)) >= min_cap)
        solver.Add(sum(x[row_idx, s, c] for row_idx, i in enumerate(data)) <= max_cap)
        
objective = solver.Objective()
for row_idx, i in enumerate(data):
    for s in programms.keys():
        for c in programms[s]:
            
            m_preferences = preferences_to_sports([i[m1], i[m2], i[m3]])
            i_preferences = preferences_to_sports([i[i1], i[i2], i[i3]])

            score = 0
            
            if s in m_preferences:
                score =  3 - m_preferences.index(s)

            elif s in i_preferences:
                score = 3 - i_preferences.index(s)

            
            objective.SetCoefficient(x[row_idx, s, c], score)

objective.SetMaximization()

status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    for row_idx, i in enumerate(data):
        for s in programms.keys():
            for c in programms[s]:    
                if x[row_idx, s, c].solution_value() > 0.5:
                    
                    semestrs_dataframes[s].loc[
                        semestrs_dataframes[s][c].notna().sum(), c
                    ] = f"{data[row_idx][nachname_idx]} {data[row_idx][vorname_idx]}"

print(semestrs_dataframes)
# for semestr, sports in programms.items():
    
#     solver = pywraplp.Solver.CreateSolver('SCIP')

#     x = {}
#     for i in data:
#         for s in sports:
#             x[i[nachname_idx], s] = solver.IntVar(0, 1, f"x_{i[nachname_idx]}_{s}")

#     for i in data:
#         solver.Add(sum(x[i[nachname_idx], s] for s in sports) == 1)
        
#     for s in sports:
#         solver.Add(sum(x[i[nachname_idx], s] for i in data) >= min_cap)
#         solver.Add(sum(x[i[nachname_idx], s] for i in data) <= max_cap)

#     objective = solver.Objective()
#     for i in data:
#         for s in sports:
            
#             m_preferences = preferences_to_sports([i[m1], i[m2], i[m3]])
#             i_preferences = preferences_to_sports([i[i1], i[i2], i[i3]])
            
#             if s in m_preferences:
#                 objective.SetCoefficient(x[i[nachname_idx], s], 3 - m_preferences.index(s))

#             elif s in i_preferences:
#                 objective.SetCoefficient(x[i[nachname_idx], s], 3 - i_preferences.index(s))

#     objective.SetMaximization()

#     status = solver.Solve()

#     if status == pywraplp.Solver.OPTIMAL:
#         for i in data:
#             for s in sports:
#                 if x[i[nachname_idx], s].solution_value() > 0.5:
#                     semestrs_dataframes[semestr].loc[
#                         semestrs_dataframes[semestr][s].notna().sum(), s
#                     ] = f"{i[nachname_idx]} {i[vorname_idx]}"

# for semestr, schedule in semestrs_dataframes.items():
    
#     print(f"{semestr}\n{schedule}")




# # Создаём решатель
# solver = pywraplp.Solver.CreateSolver('SCIP')

# # Данные
# num_students = 5
# num_semesters = 3
# num_sports = 3
# min_cap = 0
# max_cap = 2

# # preferences[i][s][c] = предпочтение студента i для спорта c в семестре s
# preferences = [
#     [  # Студент 0
#         [10, 5, 0],  # Семестр 1
#         [5, 10, 0],  # Семестр 2
#         [0, 5, 10]   # Семестр 3
#     ],
#     [  # Студент 1
#         [0, 10, 5],
#         [10, 0, 5],
#         [5, 0, 10]
#     ],
#     [  # Студент 2
#         [5, 0, 10],
#         [0, 10, 5],
#         [10, 5, 0]
#     ],
#     [  # Студент 3
#         [10, 0, 5],
#         [5, 10, 0],
#         [0, 5, 10]
#     ],
#     [  # Студент 4
#         [5, 10, 0],
#         [0, 5, 10],
#         [10, 0, 5]
#     ]
# ]

# x = {}
# for i in range(num_students):
#     for s in range(num_semesters):
#         for c in range(num_sports):
#             x[i, s, c] = solver.IntVar(0, 1, f"x_{i}_{s}_{c}")


    
# for s in range(num_semesters):
#     for c in range(num_sports):
#         solver.Add(sum(x[i, s, c] for i in range(num_students)) >= min_cap)
#         solver.Add(sum(x[i, s, c] for i in range(num_students)) <= max_cap)
    
# for i in range(num_students):
#     for s in range(num_semesters):
#         solver.Add(sum(x[i, s, c] for c in range(num_sports)) == 1)
    
# objective = solver.Objective()

# for i in range(num_students):
#     for s in range(num_semesters):
#         for c in range(num_sports):
#             objective.SetCoefficient(x[i, s, c], preferences[i][s][c])

# objective.SetMaximization()

# status = solver.Solve()


# if status == pywraplp.Solver.OPTIMAL:
#     for i in range(num_students):
#         for s in range(num_semesters):
#             for c in range(num_sports):
#                 if x[i,s,c].solution_value() > 0.5:
#                     print(f"Student {i} -> Semester {s+1}, Sport {c+1} (score {preferences[i][s][c]})")
#     print("Total happiness:", objective.Value())
# else:
#     print("Решение не найдено")
