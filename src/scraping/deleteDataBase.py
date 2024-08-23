import os

# Deleting the database

def confirm_deletion():
    confirmation = input("Are you sure you want to delete the database? Type 'yes' to confirm: ")
    return confirmation.lower() == 'yes'

def delete_database(db_path):
    if os.path.exists(db_path):
        os.remove(db_path)
        print(f"Database '{db_path}' has been deleted.")
    else:
        print(f"Database '{db_path}' does not exist.")

def main():
    db_folder = 'occupancy_data'
    db_name = 'gym_occupancy_data.db'  
    db_path = os.path.join(db_folder, db_name)
    if confirm_deletion():
        delete_database(db_path)
    else:
        print("Operation canceled. The database was not deleted.")

if __name__ == "__main__":
    main()