from reactpy import component, html
from reactpy.backend.sanic import Sanic
from reactpy.backend.sanic import configure
from Frontend.home import HomeScreen
from Frontend.movie import MovieScreen
from Frontend.user import UserProfile

# from Connection import get_db_connection


# conn = get_db_connection()

app = Sanic("MyApp")
configure(app, UserProfile)


if __name__ == "__main__":
    app.run(port=8000)
    