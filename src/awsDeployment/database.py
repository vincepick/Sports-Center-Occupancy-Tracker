import os
import mysql.connector

# For setting up the connection to the AWS RDS database in AWS Lambda 
# Then inserting the data

# Takes the data to be entered as method variables
def insert_data_to_db(occupancy_number, current_time_bst, current_day_bst, current_date_bst, temp_text, humidity_text, rain_text, wind_text):
    db_host = os.getenv('DB_HOST')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_database = os.getenv('DB_DATABASE')

    cnx = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_database
    )

    cursor = cnx.cursor()

    # Query used to insert scraped data into the DB
    insert_query = """
    INSERT INTO occupancy_data (
        percentage_column, bst_time, day_of_week, current_date_bst, temperature, humidity, chance_of_rain, wind
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    # Retrieving the values for the scraped data 
    values = (occupancy_number, current_time_bst, current_day_bst, current_date_bst, temp_text, humidity_text, rain_text, wind_text)
    
    cursor.execute(insert_query, values)
    cnx.commit()

    cursor.close()
    cnx.close()
