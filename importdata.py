from Connection import get_db_connection
from dotenv import load_dotenv
import csv

load_dotenv()

conn = get_db_connection()

file_path = 'imdb-movies-dataset.csv'

with open(file_path, 'r', newline='', encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile)

    for i, r in enumerate(csvreader):
        for t in r:
            print(r)
        name = r[1]
        desc = r[7]
        year = r[2]
        rtng = r[6]
        crtc = r[8]
        gnre = r[4]
