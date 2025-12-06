from reactpy import component, html
from Frontend.movie import HomeBtn, UpvoteBtn, DownvoteBtn


@component
def UserProfile():
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
        HomeBtn(),
        html.h1(
            {
                "style": {
                    "fontSize": "48px"
                }
            },  
            "USERNAME"
        ),
        html.p("EMAIL (OPTIONAL)"),
        Review(),
        Review(),
        Review()
        
    )
    
@component
def Review():
    return html.div(
        {
            "style": {
                "display": "flex",
                "flexDirection": "column",
                "justifyContent": "start",   
                "alignItems": "start",       
                "height": "10vh",
                "width": "60vw",                       
            }
        },
        html.div(
            {
                "style":{
                    "display": "flex",
                    "flexDirection": "row",
                    "justifyContent": "start",
                    "alignItems": "center",
                    "gap": "8px"
                }
            },
            html.p("Review for: MOVIE"),
            MovieBtn(),
        ),
        
        html.div(
            {
                "style":{
                    "display": "flex",
                    "flexDirection": "row",
                    "justifyContent": "start",
                    "alignItems": "center",
                    "gap":"8px"
                }
            },
            html.p("REVIEW"),
            UpvoteBtn(),
            DownvoteBtn()
        )
    )
    
#button to go to the movie of the review
@component
def MovieBtn():
    def btn_click(event):
        print("go to movie")
    return html.button(
        {"on_click": btn_click},
        "Movie"
    )