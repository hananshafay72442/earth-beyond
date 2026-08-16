# db.py
import mysql.connector
from mysql.connector import Error

def get_db_connection():
    """Returns a new MySQL connection. Caller is responsible for closing it."""
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="your_db_user",
            password="your_db_password",
            database="earth_beyond"
        )
        return conn
    except Error as e:
        print(f"Database connection error: {e}")
        raise