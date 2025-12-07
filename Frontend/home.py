from reactpy import component, html

@component
def HomeScreen(movies, on_select_movie):
    return html.div(
        {
            "style": {
                "display": "flex",
                "flexDirection": "column",
                "justifyContent": "start",   
                "alignItems": "start",       
                "height": "100vh",            
                "gap": "12px",
                "paddingLeft": "12px"                
            }
        },
        html.h1(
            {
                "style": {
                    "fontSize": "48px"
                }
            },  
            "Movie Review Compatibility"),
         [
            Movie(movie=m, on_select=lambda e, m=m: on_select_movie(m), key=i)
            for i, m in enumerate(movies)
        ]
    )
    
# Movie component for home page. Gives basic information
@component
def Movie(movie, on_select):
    return html.div(
        {
            "style": {
                    "display": "flex",
                    "flexDirection": "column",
                    "justifyContent": "start",   
                    "alignItems": "start",       
                    "height": "90vh",
                    "width": "30vw",                       
                }
        },
        html.div(
            {
                "style": {
                    "display": "flex",
                    "flexDirection": "row",
                    "alignItems": "center",
                    "gap": "16px"
                }
            },
            html.h2(movie.name),
            html.h3(f"({movie.releasedate})")
        ),
        html.div(
            {
                "style": {
                    "display": "flex",
                    "flexDirection": "row",
                    "gap": "4px"
                }
            },
            html.p("Directed By:"),
            html.p(movie.director)
        ),
        html.div(
            {
                "style": {
                    "display": "flex",
                    "flexDirection": "row",
                    "gap": "4px"
                }
            },
            html.p("Genre:"),
            html.p(movie.genre)
        ),
        html.div(
            {
                "style": {
                    "display": "flex",
                    "flexDirection": "row",
                    "gap": "24px"
                }
            },
            html.div(
                {
                    "style": {
                        "display": "flex",
                        "flexDirection": "row",
                        "gap": "4px"
                    }
                },
                html.p("Rating:"),
                html.p(movie.rating)
            ),
            html.div(
                {
                    "style": {
                        "display": "flex",
                        "flexDirection": "row",
                        "gap": "4px"
                    }
                },
                html.p("Critic Score:"),
                html.p(movie.criticscore)
            ),
        ),
        html.p(movie.description),
        html.button({"on_click": on_select}, "Go to movie")
    )

