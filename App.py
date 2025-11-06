from reactpy import component, html
from reactpy.backend.sanic import Sanic
from reactpy.backend.sanic import configure
from Connection import get_db_connection

conn = get_db_connection()

@component
def HelloWorld():
    return html.h1("Hello, world!")


app = Sanic("MyApp")
configure(app, HelloWorld)


if __name__ == "__main__":
    app.run(port=8000)