import pymysql
import random
import string
from datetime import datetime, timedelta

# RDS settings
REGION = 'us-east-2'
rds_host = 'database-1.craysy60cdwy.us-east-2.rds.amazonaws.com'
name = 'admin'
password = 'shu8Ren8'
db_name = 'occupancy-db'
port = 3306  # Default MySQL port

def create_table():
    # Connect to the MySQL database
    try:
        conn = pymysql.connect(
            host=rds_host,
            user=name,
            password=password,
            db=db_name,
            port=port,
            connect_timeout=5
        )
    except pymysql.MySQLError as e:
        print(f"ERROR: Unexpected error: Could not connect to MySQL instance. {e}")
        return

    print("SUCCESS: Connection to RDS MySQL instance succeeded")

    # Create a cursor object
    try:
        with conn.cursor() as cur:
            # Create table if it doesn't exist
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
            )
            """
            cur.execute(create_table_query)
            conn.commit()
            print("SUCCESS: Table 'occupancy_data' was created (if it didn't already exist).")
    except pymysql.MySQLError as e:
        print(f"ERROR: Could not create table. {e}")
    finally:
        conn.close()

def insert_random_values():
    # Connect to the MySQL database
    try:
        conn = pymysql.connect(
            host=rds_host,
            user=name,
            password=password,
            db=db_name,
            port=port,
            connect_timeout=5
        )
    except pymysql.MySQLError as e:
        print(f"ERROR: Unexpected error: Could not connect to MySQL instance. {e}")
        return

    # Generate random values
    percentage_column = random.randint(0, 100)
    bst_time = (datetime.now() + timedelta(hours=1)).strftime('%H:%M:%S')  # Assuming BST is UTC+1
    day_of_week = random.choice(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    current_date_bst = (datetime.now() + timedelta(hours=1)).strftime('%Y-%m-%d')
    temperature = f"{random.randint(-10, 35)}°C"
    humidity = f"{random.randint(10, 100)}%"
    chance_of_rain = f"{random.randint(0, 100)}%"
    wind = f"{random.randint(0, 50)} km/h"

    # Insert random values into the table
    try:
        with conn.cursor() as cur:
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
            cur.execute(insert_query, (percentage_column, bst_time, day_of_week, current_date_bst, temperature, humidity, chance_of_rain, wind))
            conn.commit()
            print("SUCCESS: Random values were inserted into 'occupancy_data' table.")
    except pymysql.MySQLError as e:
        print(f"ERROR: Could not insert values into table. {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    create_table()
    insert_random_values()
