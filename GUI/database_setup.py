import sqlite3

connection = sqlite3.connect('./GUI/fair_einwahl.db')
cursor = connection.cursor()

cursor.execute("""
               CREATE TABLE plans (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT
                   
               )
               """)

# cursor.execute("DROP TABLE plans")

cursor.execute("""
               CREATE TABLE plan_config (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   plan_id INTEGER,
                   max_capacity INTEGER,
                   min_capacity INTEGER,
                   sports_json TEXT,
                   semestrs_json TEXT,
                   slots_json TEXT,
                   FOREIGN KEY (plan_id) REFERENCES plans(id) ON DELETE CASCADE
               )
               """)

connection.commit()
connection.close()