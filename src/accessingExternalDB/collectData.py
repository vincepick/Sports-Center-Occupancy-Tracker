import string
from datetime import datetime, timedelta
import os
import mysql.connector
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

# Saves the data located in the DB as a csv to work with locally
def collectData():
    db_host = os.getenv('DB_HOST')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_database = os.getenv('DB_DATABASE')

    # Connect to the MySQL database
    cnx=mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_database
    )

    # Load the data into a Pandas DataFrame
    query = "SELECT * FROM occupancy_data"
    df = pd.read_sql_query(query, cnx)

    # Close the connection
    cnx.close()

    df['bst_time'] = df['bst_time'].apply(lambda x: int(datetime.strptime(x, '%H:%M').hour) * 60 + int(datetime.strptime(x, '%H:%M').minute))

    # Convert 'day_of_week' to corresponding integers for tensorflow
    df['day_of_week'] = df['day_of_week'].map({
        'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6
    })

    # Clean data and convert to integers to later be used by tensorflow
    df['temperature'] = df['temperature'].str.replace('°', '').astype(int)
    df['humidity'] = df['humidity'].str.replace('%', '').astype(int)
    df['chance_of_rain'] = df['chance_of_rain'].str.replace('%', '').astype(int)
    df['wind'] = df['wind'].str.replace(' km/h', '').astype(int)

    current_date = datetime.now().strftime('%Y-%m-%d')

    # Create the filename with the current date
    filename = f"occupancy_data/awsDBdata/convertedAWSdata_{current_date}.csv"

    # Save the DataFrame to a CSV file for later use
    df.to_csv(filename, index=False)

    print("Data has been successfully saved to a CSV '")

if __name__ == "__main__":
    collectData()