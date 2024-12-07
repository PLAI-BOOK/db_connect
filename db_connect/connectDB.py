import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_db_connection(db_host=None,db_user=None,db_port=None,db_password=None,db_name=None):
    """Establish a connection to the database."""
    DB_HOST = db_host or os.getenv("DB_HOST")
    DB_USER = db_user or os.getenv("DB_USER")
    DB_PORT = db_port or os.getenv("DB_PORT")
    DB_PASSWORD = db_password or os.getenv("DB_PASSWORD")
    DB_NAME = db_name or os.getenv("DB_NAME").lower()

    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn
    except Exception as e:
        print(f"Error while connecting to the {DB_NAME} database: {e}")
        return None