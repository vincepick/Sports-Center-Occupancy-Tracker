import tensorflow as tf
import numpy as np
import pandas as pd
from datetime import datetime
from tensorflow.keras.models import load_model

model = tf.keras.models.load_model('model/gym_occupancy_model.keras')


# No day value
test_data = pd.DataFrame({
    'temperature': [17],  
    'humidity': [75],    
    'chance_of_rain': [50], 
    'wind': [25],  
    'bst_time': [600]

})



# Make predictions
predicted_occupancy = model.predict(test_data)

# Convert the predicted value back to percentage
predicted_occupancy_percentage = predicted_occupancy[0][0] * 100
print(f"Predicted occupancy percentage: {predicted_occupancy_percentage:.2f}%")