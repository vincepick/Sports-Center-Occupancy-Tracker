import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Load dataset
filename = "occupancy_data/awsDBdata/convertedAWSdata_2024-09-06.csv"
df = pd.read_csv(filename)

# Remove unnecessary columns
df = df.drop(['current_date_bst', 'day_of_week', 'id'], axis=1)

# Separate target and features
target = df.pop('percentage_column')

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(df, target, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
# scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Build neural network 
model = Sequential([
    Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.2),
    Dense(64, activation='relu'),
    Dense(32, activation='relu'),
    Dense(1)
])

# Compile the model with MAE loss function
model.compile(optimizer='adam', loss='mae', metrics=['mae'])

# Train the model
history = model.fit(X_train, y_train, epochs=100, validation_split=0.2, batch_size=32)

# Evaluate model
test_loss, test_mae = model.evaluate(X_test, y_test)
print(f"Test Loss: {test_loss}, Test MAE: {test_mae}")

# Make prediction
predictions = model.predict(X_test)

# Save  model
model_name = input("Enter the name to save the model: ")
model_path = f"models/{model_name}.keras"

# Save model
model.save(model_path)

print(f"Model saved as {model_path}")

print(predictions)
