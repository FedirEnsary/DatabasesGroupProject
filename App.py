from reactpy import component, html, use_state
from reactpy.backend.sanic import Sanic
from reactpy.backend.sanic import configure
from Frontend.home import HomeScreen
from Frontend.movie import MovieScreen
from Frontend.user import UserProfile

from Connection import get_db_connection
from Connection import get_db_connection
from DBqueries import *

conn = get_db_connection()

@component
def HelloWorld():
    result = FetchRandomMovie(conn, 10)
    return html.div(
        [
            html.div({"key": i, "class_name": "movie-div"}, m.toHtml())
            for i, m in enumerate(result)
        ]
    )

@component
def Root():
    page, set_page = use_state("home")
    selected_movie, set_selected_movie, selected_user, set_selected_user = use_state(None)
    movies = FetchRandomMovie(conn, 10)
    
    if page == "home":
        return HomeScreen(
            movies=movies,
            on_select_movie=lambda movie: (set_selected_movie(movie), set_page("movie"))
        )
        
    elif page == "user":
        reviews = FetchUserReviews(conn, selected_user)
        return UserProfile(
            username=selected_user,
            reviews=reviews,
            go_home=lambda: set_page("home"),
            go_to_movie=lambda movie: (set_selected_movie(movie), set_page("movie"))
        )

    # MOVIE PAGE
    elif page == "movie":
        return MovieScreen(
            movie=selected_movie,
            go_home=lambda: set_page("home")
        )

app = Sanic("MyApp")
configure(app, Root)


if __name__ == "__main__":
    app.run(port=8000)

