
import os
import sqlite3
from datetime import datetime, timezone
print("Current working directory:", os.getcwd())
conn = sqlite3.connect('occupancy_data/gym_occupancy_data.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS occupancy_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        percentage_column INTEGER,
        bst_time TEXT,
        day_of_week TEXT,
        current_date_bst TEXT,
        temperature TEXT,
        humidity TEXT,
        chance_of_rain TEXT,
        wind TEXT
    )
''')





conn.commit()
conn.close()

print("Database and table initialized successfully.")