from reactpy import component, html
from reactpy.backend.sanic import Sanic
from reactpy.backend.sanic import configure
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


app = Sanic("MyApp")
configure(app, HelloWorld)


if __name__ == "__main__":
    app.run(port=8000)

