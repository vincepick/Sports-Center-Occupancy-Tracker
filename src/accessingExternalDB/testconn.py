import os
import json
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


# This is a program used to test the connection to the AWS hosted DB, by connecting then inserting the value 5 into each column of the DB

def main():
    db_host = os.getenv('DB_HOST')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_database = os.getenv('DB_DATABASE')

    cnx=mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_database
    )

    cursor = cnx.cursor()

    # Create the table if it does not exist
    create_table_query = """
    CREATE TABLE IF NOT EXISTS occupancy_data (
        id INT AUTO_INCREMENT PRIMARY KEY,
        percentage_column INT,
        bst_time VARCHAR(255),
        day_of_week VARCHAR(255),
        current_date_bst VARCHAR(255),
        temperature VARCHAR(255),
        humidity VARCHAR(255),
        chance_of_rain VARCHAR(255),
        wind VARCHAR(255)
    );
    """
    cursor.execute(create_table_query)

    # Insert a row with '5' in each column
    insert_query = """
    INSERT INTO occupancy_data (
        percentage_column,
        bst_time,
        day_of_week,
        current_date_bst,
        temperature,
        humidity,
        chance_of_rain,
        wind
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    # Values to insert
    values = ('5', '5', '5', '5', '5', '5', '5', '5')
    
    cursor.execute(insert_query, values)

    # Commit the transaction
    cnx.commit()

    cursor.close()
    cnx.close()
 
if __name__ == "__main__":
    main()