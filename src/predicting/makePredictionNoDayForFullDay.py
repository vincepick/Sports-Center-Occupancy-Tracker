import tensorflow as tf
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model

# Load your trained model
model = load_model('models/janDataThirdIteration.keras')

# Define the range of hours from 9 AM (09:00) to 10 PM (22:00)
hours = range(9, 23)  

# Prepare a list to store the results
results = []

for hour in hours:
    # Convert hour to minutes after midnight
    bst_time = hour * 60
    
    # Create the test data DataFrame
    test_data = pd.DataFrame({
        'temperature': [17],
        'humidity': [75],
        'chance_of_rain': [50],
        'wind': [25],
        'bst_time': [bst_time]
    })
    
    # Make a prediction
    predicted_occupancy = model.predict(test_data)
    
    # Convert the predicted value back to a percentage
    predicted_occupancy_percentage = float(predicted_occupancy[0][0]) / 100.0
    
    # Append the results (you can include any other fields you need)
    results.append({
        'hour': f"{hour}:00",
        'bst_time': bst_time,
        'predicted_occupancy_percentage': predicted_occupancy_percentage
    })

# Convert all results into a DataFrame
results_df = pd.DataFrame(results)

# Save the results to a CSV file
results_df.to_csv('prediction_results.csv', index=False)

print("Predictions from 9 AM to 10 PM have been saved to 'prediction_results.csv'.")
