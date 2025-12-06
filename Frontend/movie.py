from reactpy import component, html

@component
def MovieScreen():
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
            "MOVIE NAME (YEAR)"
        ),
        MovieInfo()
    )

#movie informaiton that is show on the home page
@component
def MovieInfo():
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
        Review() #display the reviews here
        
    )

#individual movie review
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
        html.p("USER"),
        UserBtn(),
        html.div(
            {
                "style":{
                    "display": "flex",
                    "flexDirection": "row",
                    "justifyContent": "start",
                    "alignItems": "center"
                }
            },
            html.p("REVIEW"),
            UpvoteBtn(),
            DownvoteBtn()
        )
    )
    
#upvote and downvote buttons for a review
@component
def UpvoteBtn():
    def btn_click(event):
        print("upvote review")
    return html.button(
        {"on_click": btn_click},
        "Upvote"
    ) 
    
@component
def DownvoteBtn():
    def btn_click(event):
        print("downvote review")
    return html.button(
        {"on_click": btn_click},
        "Downvote"
    ) 

#button for viewing user profile
@component
def UserBtn():
    def btn_click(event):
        print("view user profile")
    return html.button(
        {"on_click": btn_click},
        "User Profile"
    ) 
    
@component
def HomeBtn():
    def btn_click(event):
        print("go home")
    return html.button(
        {"on_click": btn_click},
        "Home"
    )

