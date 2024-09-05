import mysql.connector

def main():
    # Connect to the database
    cnx = mysql.connector.connect(
        host='occupancy-db.craysy60cdwy.us-east-2.rds.amazonaws.com',
        user='admin',
        password='shu8Ren8',
        database='occupancy_schema'
    )

    cursor = cnx.cursor()

    # Query to delete rows where 'bst_time' is NULL
    delete_query = """
    DELETE FROM occupancy_data
    WHERE id = 1
    """
    
    cursor.execute(delete_query)

    # Commit the transaction
    cnx.commit()

    # Close cursor and connection
    cursor.close()
    cnx.close()
 
if __name__ == "__main__":
    main()
