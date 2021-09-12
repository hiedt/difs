import sqlite3
from sqlite3 import Error as SQLiteConnectionError


def connect_db(db_name):
    """
    Connect our program with a database (.db file)

    Args:
        db_name (str): Path to .db file
    """
    db = None
    try:
        db = sqlite3.connect(db_name)
        print(f"Finish connecting with database {db_name}")
    except SQLiteConnectionError:
        print(SQLiteConnectionError)
    
    return db


db = connect_db("database/chinook.db") # *Global variable
curs = db.cursor() # Create cursor object to execute queries
