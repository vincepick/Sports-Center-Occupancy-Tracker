import sqlite3
import pandas as pd
from datetime import datetime

# Program used to query local sqlite DB and convering it into a DF

# Connect to the SQLite database
conn = sqlite3.connect('occupancy_data/gym_occupancy_data.db')

# Load the data into a Pandas DataFrame
query = "SELECT * FROM occupancy_data"
df = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

# Convert 'bst_time' to number of minutes since midnight
df['bst_time'] = df['bst_time'].apply(lambda x: int(datetime.strptime(x, '%H:%M').hour) * 60 + int(datetime.strptime(x, '%H:%M').minute))

# Convert 'day_of_week' to corresponding integers for tensorflow
df['day_of_week'] = df['day_of_week'].map({
    'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6
})

# Clean data and convert to integers to later be used by tensorflow
df['temperature'] = df['temperature'].str.replace('°', '').astype(int)
df['humidity'] = df['humidity'].str.replace('%', '').astype(int)
df['chance_of_rain'] = df['chance_of_rain'].str.replace('%', '').astype(int)
df['wind'] = df['wind'].astype(int)

# Save the DataFrame to a CSV file for later use
df.to_csv('converted_data.csv', index=False)