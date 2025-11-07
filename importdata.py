from Connection import get_db_connection
from dotenv import load_dotenv
import csv

load_dotenv()

conn = get_db_connection()

file_path = 'imdb_top_1000.csv'

with open(file_path, 'r', newline='', encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile)

    for i, r in enumerate(csvreader):
        print(r)