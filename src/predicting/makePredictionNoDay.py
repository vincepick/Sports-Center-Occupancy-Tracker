import tensorflow as tf
import numpy as np
import pandas as pd
from datetime import datetime
from tensorflow.keras.models import load_model

model = tf.keras.models.load_model('gym_occupancy_model.h5')


# No day value
test_data = pd.DataFrame({
    'temperature': [17],  
    'humidity': [75],    
    'chance_of_rain': [50], 
    'wind': [25],  
    'bst_time': [600]

})

# Guess occupancy for new data using the same model used to make the training data
predicted_occupancy = model.predict(test_data)
print(f"Predicted occupancy percentage: {predicted_occupancy[0][0]:.2f}%")