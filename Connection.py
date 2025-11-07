import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=os.environ.get('PG_HOST', os.getenv("host")),
            database=os.environ.get('PG_DB', os.getenv("database")),
            user=os.environ.get('PG_USER', os.getenv("user")),
            password=os.environ.get('PG_PASSWORD', os.getenv("password"))
        )
        print(f"Database connection successful")
        return conn
    except psycopg2.DatabaseError as e:
        print(f"Database connection error: {e}")
        return None