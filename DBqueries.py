from Classes import *
import Connection
import bcrypt
from InfernalMachine import CompareReviews

#Bcrypt Hashing

def hashPassword(password):
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed

def verifyPassword(hashedPassword, providedPassword):
    return bcrypt.checkpw(providedPassword.encode('utf-8'), hashedPassword)

#Find and Manage Movies

def FetchMovie(conn, name) -> movie:
    cur = conn.cursor()
    cur.execute("Select * from movies where name = \'" + name.replace("\'", "\'\'") + "\';")
    result = cur.fetchall()
    return movie(result[0][0], result[0][1], result[0][2], result[0][3], result[0][4], result[0][5], result[0][6])

def FetchRandomMovie(conn, count=1):
    cur = conn.cursor()
    cur.execute("SELECT * FROM movies WHERE name IN (SELECT name FROM movies ORDER BY random() LIMIT " + str(count) + ");")
    result = cur.fetchall()
    resultingMovies = []
    for curr in result:
        resultingMovies.append(movie(curr[0], curr[1], curr[2], curr[3], curr[4], curr[5], curr[6]))
    return resultingMovies

def AddMovie(conn, name, desc="", year=0, rtng=0.0, crtc=0, gnre="", drct=""):
    if(name == ""):
        return "Please provide a movie name."
    cur = conn.cursor()
    cur.execute("Select * from movies where name = \'" + name.replace("\'", "\'\'") + "\';")
    if(len(cur.fetchall()) > 0):
        return "A movie under the name " + name + " already exists in the database."
    query = "INSERT INTO Movies (name, description, releasedate, rating, criticscore, genre, director) VALUES (\'" + name.replace("\'", "\'\'") + "\', \'" + desc.replace("\'", "\'\'") + "\', " + str(year) + ", " + str(rtng) + ", " + str(crtc) + ", \'" + gnre.replace("\'", "\'\'") + "\', \'" + drct.replace("\'", "\'\'") + "\');"
    try:
        cur.execute(query)
        conn.commit()
        return name + " added to movies Sucessfully."
    except psycopg2.Error as e:
        conn.rollback()
        return "Error adding movie: " + e

def DeleteMovie(conn, name):
    cur = conn.cursor()
    cur.execute("Select * from movies where name = \'" + name.replace("\'", "\'\'") + "\';")
    if(len(cur.fetchall()) == 0):
        return "There is no movie " + name + ", please make sure there are no typos."
    query = "DELETE FROM movies WHERE name = \'" + name.replace("\'", "\'\'") + "\';"
    try:
        cur.execute(query)
        conn.commit()
        return "Removed movie Sucessfully."
    except psycopg2.Error as e:
        conn.rollback()
        return "Error removing movie: " + e

def SearchMovie(conn, name):
    cur = conn.cursor()
    cur.execute("SELECT * FROM movies WHERE name like '%" + name.replace("\'", "\'\'") + "%' limit 50;")
    result = cur.fetchall()
    resultingMovies = []
    for curr in result:
        resultingMovies.append(movie(curr[0], curr[1], curr[2], curr[3], curr[4], curr[5], curr[6]))
    return resultingMovies

def ChangeMovieRating(conn, name, rating):
    cur = conn.cursor()
    cur.execute("Select * from  movies where name = \'" + name.replace("\'", "\'\'") + "\';")
    if(len(cur.fetchall()) == 0):
        return "We do not have a movie " + name + ", please make sure there are no typos."
    query = "UPDATE movies SET Rating = " + str(rating) + " WHERE name = \'" + name.replace("\'", "\'\'") + "\';"
    try:
        cur.execute(query)
        conn.commit()
        return "Updated rating Sucessfully."
    except psycopg2.Error as e:
        conn.rollback()
        return "Error updating rating: " + e

def ChangeCriticScore(conn, name, criticscore):
    cur = conn.cursor()
    cur.execute("Select * from  movies where name = \'" + name.replace("\'", "\'\'") + "\';")
    if(len(cur.fetchall()) == 0):
        return "We do not have a movie " + name + ", please make sure there are no typos."
    query = "UPDATE movies SET criticscore = " + str(criticscore) + " WHERE name = \'" + name.replace("\'", "\'\'") + "\';"
    try:
        cur.execute(query)
        conn.commit()
        return "Updated rating Sucessfully."
    except psycopg2.Error as e:
        conn.rollback()
        return "Error updating rating: " + e

#Find and Manage Top Reviews

def FetchTopReview(conn, title) -> topReview:
    cur = conn.cursor()
    cur.execute("Select * from topreviews where title = \'" + title.replace("\'", "\'\'") + "\';")
    result = cur.fetchall()
    return topReview(result[0][0], result[0][1], result[0][2], result[0][3])

def AddTopReview(conn, name, text = "", rating = 0, title = ""):
    if(name == ""):
        return "Please provide a movie name."
    if(len(text) < 20):
        return "Please provide a more meaningful review."
    cur = conn.cursor()
    cur.execute("Select * from movies where name = \'" + name.replace("\'", "\'\'") + "\';")
    if(len(cur.fetchall()) == 0):
        return "We do not have " + name + " as a movie, please make sure there are no typos, or add the movie to the out database."
    query = "INSERT INTO topreviews (text, rating, title, name) VALUES (\'" + text.replace("\'", "\'\'") + "\', " + str(rating) + ", \'" + title.replace("\'", "\'\'") + "\', \'" + name.replace("\'", "\'\'") + "\');"
    try:
        cur.execute(query)
        conn.commit()
        return "Added to top reviews Sucessfully."
    except psycopg2.Error as e:
        conn.rollback()
        return "Error adding review: " + e

def DeleteTopReview(conn, name):
    cur = conn.cursor()
    cur.execute("Select * from topreviews where name = \'" + name.replace("\'", "\'\'") + "\';")
    if(len(cur.fetchall()) == 0):
        return "We do not have a top review for " + name + ", please make sure there are no typos."
    query = "DELETE FROM topreviews WHERE name = \'" + name.replace("\'", "\'\'") + "\';"
    try:
        cur.execute(query)
        conn.commit()
        return "Removed from top reviews Sucessfully."
    except psycopg2.Error as e:
        conn.rollback()
        return "Error removing review: " + e

def ChangeTopReviewRating(conn, name, rating):
    cur = conn.cursor()
        cur.execute("Select * from  topreviews where name = \'" + name.replace("\'", "\'\'") + "\';")
        if(len(cur.fetchall()) == 0):
            return "We do not have a movie " + name + ", please make sure there are no typos."
        query = "UPDATE movies SET Rating = \'" + str(rating) + "\' WHERE name = \'" + name.replace("\'", "\'\'") + "\';"
        try:
            cur.execute(query)
            conn.commit()
            return "Updated review rating Sucessfully."
        except psycopg2.Error as e:
            conn.rollback()
            return "Error updating review rating: " + e

#Find and Manage Reviews

def FetchMovieReviews(conn, title):
    cur = conn.cursor()
    cur.execute("Select * from userreviews where title = \'" + title.replace("\'", "\'\'") + "\';")
    result = cur.fetchall()
    resultingReviews = []
    for curr in result:
        resultingReviews.append(review(curr[0], curr[1], curr[2], curr[3], curr[4], curr[5], curr[6]))
    return resultingReviews

def FetchUserReviews(conn, username):
    cur = conn.cursor()
    cur.execute("Select * from userreviews where username = \'" + username + "\';")
    result = cur.fetchall()
    resultingReviews = []
    for curr in result:
        resultingReviews.append(review(curr[0], curr[1], curr[2], curr[3], curr[4], curr[5], curr[6]))
    return resultingReviews

def AddReview(conn, username, text, title, rating = 0):
    if(title == ""):
        return "Please provide a movie name."
    if(len(text) < 20):
        return "Please provide a more meaningful review."
    cur = conn.cursor()
    cur.execute("Select * from movies where name = \'" + name.replace("\'", "\'\'") + "\';")
    if(len(cur.fetchall()) == 0):
        return "We do not have " + name + " as a movie, please make sure there are no typos, or add the movie to the out database."
    cur.execute("Select * from users where username = \'" + username.replace("\'", "\'\'") + "\';")
    if(len(cur.fetchall()) == 0):
        return "The user " + username + " does not exist, please make sure there are no typos."
    query = "INSERT INTO userreviews (username, text, rating, name) VALUES (\'" + username.replace("\'", "\'\'") + "\', \'" + text.replace("\'", "\'\'") + "\', " + str(rating) + ", \'" + title.replace("\'", "\'\'") + "\');"
    try:
        cur.execute(query)
        conn.commit()
        return "Added to reviews Sucessfully."
    except psycopg2.Error as e:
        conn.rollback()
        return "Error adding review: " + e

def DeleteReview(conn, username, title):
    cur = conn.cursor()
    cur.execute("Select * from  userreviews where name = \'" + name.replace("\'", "\'\'") + "\' and username = \'" + username.replace("\'", "\'\'") + "\';")
    if(len(cur.fetchall()) == 0):
        return "We do not have a review for " + name + " made by " + username + ", please make sure there are no typos."
    query = "DELETE FROM userreviews WHERE name = \'" + name.replace("\'", "\'\'") + "\' and username = \'" + username.replace("\'", "\'\'") + "\';"
    try:
        cur.execute(query)
        conn.commit()
        return "Removed from reviews Sucessfully."
    except psycopg2.Error as e:
        conn.rollback()
        return "Error removing review: " + e

def EditReview(conn, username, title, text):
    cur = conn.cursor()
    cur.execute("Select * from  userreviews where name = \'" + name.replace("\'", "\'\'") + "\' and username = \'" + username.replace("\'", "\'\'") + "\';")
    if(len(cur.fetchall()) == 0):
        return "We do not have a review for " + name + " made by " + username + ", please make sure there are no typos."
    query = "UPDATE userreviews SET text = \'" + text.replace("\'", "\'\'") + "\' WHERE name = \'" + name.replace("\'", "\'\'") + "\' and username = \'" + username.replace("\'", "\'\'") + "\';"
    try:
        cur.execute(query)
        conn.commit()
        return "Updated review Sucessfully."
    except psycopg2.Error as e:
        conn.rollback()
        return "Error updating review: " + e

def ChangeReviewRating(conn, username, title, rating):
    cur = conn.cursor()
    cur.execute("Select * from userreviews where name = \'" + name.replace("\'", "\'\'") + "\' and username = \'" + username + "\';")
    if(len(cur.fetchall()) == 0):
        return "We do not have a review by " + username + " for a movie " + name + ", please make sure there are no typos."
    query = "UPDATE userreviews SET rating = \'" + str(rating) + "\' WHERE name = \'" + name.replace("\'", "\'\'") + "\' and username = \'" + username + "\';"
    try:
        cur.execute(query)
        conn.commit()
        return "Updated rating Sucessfully."
    except psycopg2.Error as e:
        conn.rollback()
        return "Error updating rating: " + e

#Find and Manage Users

def FetchUser(conn, username):
    cur = conn.cursor()
    cur.execute("Select username, email, showemail from users where username = \'" + username.replace("\'", "\'\'") + "\' limit 1;")
    result = cur.fetchall()
    if result[0][2] == "FALSE":
        return user(result[0][1])
    else:
        return user(result[0][1], result[0][2])

def SearchUser(conn, username):
    cur = conn.cursor()
    cur.execute("Select username, email, showemail from users where username like \'%" + username.replace("\'", "\'\'") + "%\';")
    result = cur.fetchall()
    resultingUsers = []
    for curr in result:
        if curr[0][2] == "FALSE":
            resultingUsers.append(user(curr[0][1]))
        else:
            resultingUsers.append(user(curr[0][1], curr[0][2]))
    return resultingUsers

def AddUser(conn, username, showemail, email, password):
    if(username == ""):
        return "Please provide a username."
    cur = conn.cursor()
    cur.execute("Select * from users where username = \'" + name.replace("\'", "\'\'") + "\';")
    if(len(cur.fetchall()) > 0):
        return "The username " + username + " is already taken."
    
    password =  hashPassword(password)
    query = "INSERT INTO users (username, password, email, showemail) VALUES (\'" + username.replace("\'", "\'\'") + "\', \'" + password.replace("\'", "\'\'") + "\', \'" + email.replace("\'", "\'\'") + "\', " + showemail + ");"
    try:
        cur.execute(query)
        conn.commit()
        return "Created user Sucessfully."
    except psycopg2.Error as e:
        conn.rollback()
        return "Error creating user: " + e

def DeleteUser(conn, username):
    if(username == ""):
        return "Please provide a username."
    cur = conn.cursor()
    cur.execute("Select * from users where username = \'" + username.replace("\'", "\'\'") + "\';")
    if(len(cur.fetchall()) == 0):
        return "There is no " + username + " as a user."
    query = "DELETE From users where username = \'" + username.replace("\'", "\'\'") + "\';"
    try:
        cur.execute(query)
        conn.commit()
        return "Deleted " + username + " Sucessfully."
    except psycopg2.Error as e:
        conn.rollback()
        return "Error deleting user: " + e

def ChangePassword(conn, username, oldpassword, newpassword):
    cur = conn.cursor()
    cur.execute("Select * from users where username = \'" + username.replace("\'", "\'\'") + "\';")
    if len(cur.fetchall()) == 0:
        return "No such user."
    cur.execute("Select * from users where username = \'" + username.replace("\'", "\'\'") + "\';")
    if verifyPassword((cur.fetchall())[0][1], oldpassword):
        query = "Update users SET password = \'" + hashPassword(newpassword) + "\' WHERE username = \'" + username.replace("\'", "\'\'") + "\';"
        try:
            cur.execute(query)
            conn.commit()
            return "Changed password sucessfully."
        except psycopg2.Error as e:
            conn.rollback()
            return "Error changing password: " + e
    else:
        return "Provided old password is incorrect."

def ChangeEmail(conn, username, password, newemail):
    cur = conn.cursor()
    cur.execute("Select * from users where username = \'" + username.replace("\'", "\'\'") + "\';")
    if len(cur.fetchall()) == 0:
        return "No such user."
    cur.execute("Select * from users where username = \'" + username.replace("\'", "\'\'") + "\';")
    if verifyPassword((cur.fetchall())[0][1], oldpassword):
        query = "Update users SET email = \'" + newemail + "\' WHERE username = \'" + username.replace("\'", "\'\'") + "\';"
        try:
            cur.execute(query)
            conn.commit()
            return "Changed email sucessfully."
        except psycopg2.Error as e:
            conn.rollback()
            return "Error changing email: " + e
    else:
        return "Provided old password is incorrect."

def ChangePreference(conn, username, password, preference):
    cur = conn.cursor()
    cur.execute("Select * from users where username = \'" + username.replace("\'", "\'\'") + "\';")
    if len(cur.fetchall()) == 0:
        return "No such user."
    cur.execute("Select * from users where username = \'" + username.replace("\'", "\'\'") + "\';")
    if verifyPassword((cur.fetchall())[0][1], oldpassword):
        query = "Update users SET showemail = " + preference + " WHERE username = \'" + username.replace("\'", "\'\'") + "\';"
        try:
            cur.execute(query)
            conn.commit()
            return "Changed email preferences sucessfully."
        except psycopg2.Error as e:
            conn.rollback()
            return "Error changing email preferences: " + e
    else:
        return "Provided old password is incorrect."

def attempLogin(conn, username, password):
    cur = conn.cursor()
    cur.execute("Select * from users where username = \'" + username.replace("\'", "\'\'") + "\';")
    result = cur.fetchall()
    if len(result) == 0:
        return "No such user."
    return verifyPassword(result[0][1], password)