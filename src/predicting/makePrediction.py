import tensorflow as tf
import numpy as np
import pandas as pd
from datetime import datetime
from tensorflow.keras.models import load_model

model = tf.keras.models.load_model('gym_occupancy_model.h5')


# Sample data which will be used to predict a value for occupancy
new_data = pd.DataFrame({
    'day_of_week': [0],  # Monday
    'temperature': [20],  # 20 degrees
    'humidity': [50],     # 50%
    'chance_of_rain': [10],  # 10% chance of rain
    'wind': [5],  # 5 km/h wind
    'bst_time': [600] # 600 minutes after midnight: 10am
})

# Normalize the new data using the same scaler used on the training data

predicted_occupancy = model.predict(new_data)
print(f"Predicted occupancy percentage: {predicted_occupancy[0][0]:.2f}%")