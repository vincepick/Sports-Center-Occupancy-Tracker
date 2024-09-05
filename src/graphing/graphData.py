import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Connect to the SQLite database
conn = sqlite3.connect('occupancy_data/gym_occupancy_data.db')
query = "SELECT * FROM occupancy_data"

# Read the data into a DataFrame
df = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

# Convert bst_time to datetime format
df['bst_time'] = pd.to_datetime(df['bst_time'])

# Group by the time and calculate the mean of percentage_column
df_avg = df.groupby(df['bst_time'].dt.time)['percentage_column'].mean().reset_index()

# Convert the time back to a datetime object for plotting
df_avg['bst_time'] = pd.to_datetime(df_avg['bst_time'].astype(str))

# Plot the data points without connecting them
plt.figure(figsize=(12, 6))
plt.scatter(df['bst_time'], df['percentage_column'], marker='o', label='Data Points')

# Plot the average line
plt.plot(df_avg['bst_time'], df_avg['percentage_column'], color='red', label='Average Line')

# Formatting the x-axis to display time throughout the day
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=1))

# Adding title and labels
plt.title('Percentage Column Over Time with Average Line')
plt.xlabel('BST Time')
plt.ylabel('Percentage')

# Rotating x-axis labels for better readability
plt.xticks(rotation=45)

# Add a legend
plt.legend()

plt.tight_layout()
plt.show()
