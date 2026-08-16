# db.py
import mysql.connector
from mysql.connector import Error
from config import Config

def get_db_connection():
    """Returns a new MySQL connection. Caller is responsible for closing it."""
    try:
        conn = mysql.connector.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            database=Config.DB_NAME
        )
        return conn
    except Error as e:
        print(f"Database connection error: {e}")
        raise