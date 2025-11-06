import psycopg2
import os
from secret import actualdatabase, actualhost, actualpassword, actualuser

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=os.environ.get('PG_HOST', actualhost),
            database=os.environ.get('PG_DB', actualdatabase),
            user=os.environ.get('PG_USER', actualuser),
            password=os.environ.get('PG_PASSWORD', actualpassword)
        )
        print(f"Database connection successful")
        return conn
    except psycopg2.DatabaseError as e:
        print(f"Database connection error: {e}")
        return None