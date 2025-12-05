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
            name = r[1].replace("\'", "\'\'")
            desc = r[11].replace("\'", "\'\'")
            year = r[2]
            if len(year) == 0:
                year = 0
            rtng = r[6]
            if len(rtng) == 0:
                rtng = 0
            crtc = r[7]
            if len(crtc) == 0:
                crtc = 0
            gnre = r[5].replace("\'", "\'\'")
            drct = r[8].replace("\'", "\'\'")
            cur.execute("Select * FROM Movies WHERE name = \'" + name + "\';")
            check = cur.fetchall()
            if len(check) < 1:
                cur.execute("INSERT INTO Movies (name, description, releasedate, rating, criticscore, genre, director) VALUES (\'" + name + "\', \'" + desc + "\', " + str(year) + ", " + str(rtng) + ", " + str(crtc) + ", \'" + gnre + "\', \'" + drct + "\');")
            else:
                print(name + " already added")
    conn.commit()    
    print("done")
    conn.close()
