import pandas as pd
import matplotlib.pyplot as plt

# Function to convert bst_time (minutes since midnight) to regular time format (AM/PM)
def convert_to_am_pm(minutes):
    hours = minutes // 60
    mins = minutes % 60
    am_pm = "AM" if hours < 12 else "PM"
    hours = hours % 12
    hours = 12 if hours == 0 else hours  # To handle the 12 PM and 12 AM case
    return f"{hours}:{mins:02d} {am_pm}"

# Read the CSV file into a DataFrame
df = pd.read_csv('occupancy_data/awsDBdata/convertedAWSdata_2024-09-15-truncated.csv')  # Replace 'your_csv_file.csv' with the actual file path

# Convert bst_time (in minutes) to readable AM/PM time for labeling
df['formatted_time'] = df['bst_time'].apply(convert_to_am_pm)

# Plot the occupancy percentage based on bst_time (minutes) and day of week
plt.figure(figsize=(10, 6))
for day in df['day_of_week'].unique():
    day_data = df[df['day_of_week'] == day]
    plt.plot(day_data['bst_time'], day_data['percentage_column'], label=f'Day {day}')

# Customize plot
plt.title('Gym Occupancy by Time and Day of the Week')
plt.xlabel('Time (AM/PM)')
plt.ylabel('Occupancy Percentage')
plt.legend(title='Day of Week')
plt.grid(True)

# Set x-axis labels to AM/PM format
xticks = df['bst_time'].unique()
plt.xticks(xticks, [convert_to_am_pm(tick) for tick in xticks], rotation=45)

# Display the plot
plt.tight_layout()
plt.show()
