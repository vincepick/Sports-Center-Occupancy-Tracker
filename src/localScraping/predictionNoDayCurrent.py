import tensorflow as tf
import numpy as np
import pandas as pd
from datetime import datetime
from tensorflow.keras.models import load_model
import sys
import os
from retrieveCurrentData import retrieveCurrentData

model = tf.keras.models.load_model('models/gym_occupancy_improved_model.keras')

scraped_data = retrieveCurrentData()

print(scraped_data)


# Convert the time (HH:MM) to minutes after 12:00 AM
time_parts = scraped_data['time'].split(':')
bst_time_minutes = int(time_parts[0]) * 60 + int(time_parts[1])

# Prepare test data for prediction, ensuring all values are in the expected format
test_data = pd.DataFrame({
    'temperature': [float(scraped_data['temperature'].replace('°', ''))],  # Clean temperature data
    'humidity': [float(scraped_data['humidity'].replace('%', ''))],          # Clean humidity data
    'chance_of_rain': [float(scraped_data['chance_of_rain'].replace('%', ''))],  # Clean chance of rain
    'wind': [float(scraped_data['wind_speed'].replace(' mph', ''))],         # Clean wind speed
    'bst_time': [bst_time_minutes]
})



# Make predictions
predicted_occupancy = model.predict(test_data)

# Convert the predicted value back to percentage
predicted_occupancy_percentage = predicted_occupancy[0][0] / 100
print(f"Predicted occupancy percentage right now: {predicted_occupancy_percentage:.2f}%")