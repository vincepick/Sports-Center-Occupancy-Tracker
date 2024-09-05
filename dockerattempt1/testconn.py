import json 
import mysql.connector

def main():
    cnx=mysql.connector.connect(
        host='occupancy-db.craysy60cdwy.us-east-2.rds.amazonaws.com',
        user='admin',
        password='shu8Ren8',
        database='occupancy_schema'
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