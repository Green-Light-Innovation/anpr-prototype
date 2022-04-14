import os
import sqlite3

class DatabaseEngine:

    connection = None
    cursor = None
    
    db_path = "./database/database.db"
    schema_path = "./database/schema.sql"

    @staticmethod
    def connect() -> None:
        """ Connect to the database file """

        # Check if database file exists
        if not os.path.exists(DatabaseEngine.db_path):
            DatabaseEngine.create_new_database()
            return
        
        DatabaseEngine.connection = sqlite3.connect(DatabaseEngine.db_path) # Create new coneciton object instance
        DatabaseEngine.cursor = DatabaseEngine.connection.cursor() # Create new cursor object instance

    @staticmethod
    def disconnect() -> None:
        """ Close connection to the database file"""

        DatabaseEngine.connection.close()
        DatabaseEngine.connection = None
        DatabaseEngine.cursor = None

    @staticmethod
    def commit() -> None:
        """ Save changes to a database after a command has been executed """
        
        if not DatabaseEngine.connection: return # Dont commit if no connection is established
        DatabaseEngine.connection.commit()

    @staticmethod
    def create_new_database() -> None:
        """ Create a new database file (only needed when original file is lost) """

        # Create a new connection
        # This also creates a new file
        DatabaseEngine.connection = sqlite3.connect(DatabaseEngine.db_path)

        # Assign new cursor object
        DatabaseEngine.cursor = DatabaseEngine.connection.cursor()

        # Read the SQL schema
        with open(DatabaseEngine.schema_path, "r") as file:
            schema = file.read()

        DatabaseEngine.cursor.execute(schema)   # Execute schema SQL on database
        DatabaseEngine.commit()      # Commit changes
        DatabaseEngine.disconnect()             # Close connection

