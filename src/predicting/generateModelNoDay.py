import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import sqlite3
import pandas as pd
from datetime import datetime
from sklearn.model_selection import train_test_split


# Connect to the SQLite database
conn = sqlite3.connect('occupancy_data/gym_occupancy_data.db')

# Load the data into a Pandas DataFrame
query = "SELECT * FROM occupancy_data"
df = pd.read_sql_query(query, conn)

# print(df)

# Close the connection
conn.close()

df['bst_time'] = df['bst_time'].apply(lambda x: int(datetime.strptime(x, '%H:%M').hour) * 60 + int(datetime.strptime(x, '%H:%M').minute))

# Convert 'day_of_week' to integers
df['day_of_week'] = df['day_of_week'].map({
    'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6
})

# Remove symbols and convert to integers
df['temperature'] = df['temperature'].str.replace('°', '').astype(int)
df['humidity'] = df['humidity'].str.replace('%', '').astype(int)
df['chance_of_rain'] = df['chance_of_rain'].str.replace('%', '').astype(int)
df['wind'] = df['wind'].astype(int)

# Remove the original datetime columns if not needed
df = df.drop(['current_date_bst', 'day_of_week', 'id'], axis=1)

print(df)

features = df.drop('percentage_column', axis=1)
target = df['percentage_column']/100.0

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
# print(df)
print('Getting to hereee!!!s')
print(X_train.dtypes)
print(y_train.dtypes)

model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.3),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')  # Single output for regression
])

model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])

# Train the model
model.fit(X_train, y_train, epochs=100, validation_split=0.2, batch_size=32)

test_loss, test_mae = model.evaluate(X_test, y_test)
print(f"Test MAe: {test_mae}")

predictions = model.predict(X_test) * 100

model.save('gym_occupancy_model.keras')







