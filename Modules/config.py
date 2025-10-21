from pathlib import Path

#file paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / 'Data'

INPUT_FILE = DATA_DIR / 'Kurseinwahl_10-1.xlsx'
# INPUT_FILE = str(DATA_DIR / 'Kurseinwahl_10-1 – copy (2).xlsx')  # alternative variat

OUTPUT_DIR = BASE_DIR / 'Output'

OUTPUT_FILE = OUTPUT_DIR / 'final_tabele.xlsx'
OUTPUT_STAT_FILE = OUTPUT_DIR / 'statistik.xlsx'

OUTPUT_DIR.mkdir(exist_ok= True)

# indexes to sports
SPORTS = {
    11: "Basketball",
    12: "Volleyball",
    13: "Fußball",
    21: "Gerätturnen",
    22: "Gymnastik/Tanz",
    23: "Leichtathletik",
    24: "Badminton",
}

# constants
MAX_CAPACITY = 30
MIN_CAPACITY = 16

# semestrs
SEMESTRS = [11.1, 11.2, 12.1]

# slots in semestrs
SLOTS = [0, 1, 2]

# total amount of groups
TOTAL_GROUPS = len(SLOTS) * len(SEMESTRS)

# fixed sport, that will be pinned to the 1th place of 1 semestr
FIXED_SPORT = SPORTS[23]  # Leichtathletik

#which way do user want to save finall tabel
FINALL_FILE_SAVE_AS = 'pdf' # 'pdf' or 'excel'

# constants for statistik
MAX_SEMESTR_SATISFACTION = 3
MAX_TOTAL_SATISFACTION = MAX_SEMESTR_SATISFACTION * len(SEMESTRS)
SATISFACTION_DISTRIBUTION = ["0-30%", "30-60%", "60-85%", "85-100%"]
TABLE_COLORS = ["#c6dbef", "#88b6ce", "#2b7cab", "#125793"]
PIE_COLORS = ["#2171b5", "#6baed6", "#9ecae1","#c6dbef"]
