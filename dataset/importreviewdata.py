from Connection import get_db_connection
from dotenv import load_dotenv
import csv

load_dotenv()

conn = get_db_connection()
cur = conn.cursor()

file_path = 'imdb-movies-dataset.csv'

with open(file_path, 'r', newline='', encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile)

    for i, r in enumerate(csvreader):
        if i == 0:
            print(r)
        else:
            name = r[13].replace("\'", "\'\'")
            title = r[1].replace("\'", "\'\'")
            rating = r[12].replace(",", "")
            text = r[14].replace("\'", "\'\'")
            cur.execute("Select * FROM topreviews WHERE name = \'" + name + "\';")
            check = cur.fetchall()
            if len(check) < 1:
                cur.execute("INSERT INTO topreviews (text, rating, title, name) VALUES (\'" + text + "\', " + rating + ", \'" + title + "\', \'" + name + "\');")
            else:
                print(name + " already added")
    conn.commit()    
    print("done")
    conn.close()
