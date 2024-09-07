import os
import json
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

# File to execute the contained query, can be used for removing entries from or otherwise manipulating the DB

def main():

    # Connect to the database using env variables
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

    # Query to delete rows where BST is null, but can be used for removing any row
    delete_query = """
    DELETE FROM occupancy_data
    WHERE id = 324
    """
    
    cursor.execute(delete_query)

    # Commit the transaction
    cnx.commit()

    # Close cursor and connection
    cursor.close()
    cnx.close()
 
if __name__ == "__main__":
    main()
