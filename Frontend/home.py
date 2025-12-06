from reactpy import component, html

@component
def HomeScreen():
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
        Movie(),
        Movie(),
        Movie()
    )
    
# Movie component for home page. Gives basic information
@component
def Movie():
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
            html.h2("MOVIE NAME"),
            html.h3("(YEAR)")
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
            html.p("DIRECTOR")
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
            html.p("GENRE")
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
                html.p("RATING")
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
                html.p("CRITIC SCORE")
            ),
        ),
        html.p("DESCRIPTION"),
        ReviewBtn()
    )

@component
def ReviewBtn():
    def btn_click(event):
        print("hi")
    return html.button(
        {"on_click": btn_click},
        "Go to movie"
    ) 