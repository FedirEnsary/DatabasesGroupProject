from Connection import get_db_connection
from DBqueries import *

conn = get_db_connection()

curr = conn.cursor()

username = "Francine"
showemail = 0
email = "Gruble@gmail.com"
password = "password"
print(AddUser(conn, username, showemail, email, password))

username = "AmandaLovesMovies"
showemail = 1
email = "Lamanda@gmail.com"
password = "password"
print(AddUser(conn, username, showemail, email, password))

username = "mark"
showemail = 1
email = "smark@gmail.com"
password = "password"
print(AddUser(conn, username, showemail, email, password))

john = FetchUser(conn, 'john')

mark = FetchUser(conn, 'mark')

hannah = FetchUser(conn, 'Hannah')

print(john.username + "\n" + str(john.email))

print(mark.username + "\n" + str(mark.email))

print(hannah.username + "\n" + str(hannah.email))

result = SearchUser(conn, "ma")

print("\nusers found:")
for user in result:
    print(user.username)

print(DeleteUser(conn, "mark"))

result = SearchUser(conn, "ma")

print("\nusers found:")
for user in result:
    print(user.username)