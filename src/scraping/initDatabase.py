
import os
import sqlite3
from datetime import datetime, timezone

# Define the directory and database paths
directory = 'occupancy_data'
database_path = os.path.join(directory, 'gym_occupancy_data.db')

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)
    print(f"Directory '{directory}' created.")

conn = sqlite3.connect(database_path)
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