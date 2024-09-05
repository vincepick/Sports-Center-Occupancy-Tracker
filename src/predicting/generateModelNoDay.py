import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import sqlite3
import pandas as pd
from datetime import datetime
from sklearn.model_selection import train_test_split



# Read from an existing dataframe
df = pd.read_csv('converted_data.csv')


# Remove the original datetime columns if not needed
df = df.drop(['current_date_bst', 'day_of_week', 'id'], axis=1)

# print(df)

# Sets features variable to contain all of the input features to train the model
target = df.pop('percentage_column')

X_train, X_test, y_train, y_test = train_test_split(df, target, test_size=0.2, random_state=42)


#Building the neural network model
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.3),
    Dense(32, activation='relu'),
    Dense(1)  
])

model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])

# Train the model, model goes through dataset 100 times, 20% used for validation, 32 different batches
model.fit(X_train, y_train, epochs=100, validation_split=0.2, batch_size=32)


test_loss, test_mae = model.evaluate(X_test, y_test)
print(f"Test MAe: {test_mae}")


predictions = model.predict(X_test)
# print('predictions')
# print(predictions)



model.save('models/gym_occupancy_model.keras')







