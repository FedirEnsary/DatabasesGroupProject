from reactpy import component, html
import router
from DBqueries import *
@component
def MovieScreen(movie, go_home, conn):
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
        HomeBtn(go_home),
        html.h1(
            {
                "style": {
                    "fontSize": "48px"
                }
            },  
            f"{movie.name} ({movie.releasedate})"
        ),
        MovieInfo(movie, conn)
    )

#movie informaiton that is show on the home page
@component
def MovieInfo(movie, conn):
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
        Review(conn, movie.name) #display the reviews here
        
    )

#individual movie review
@component
def Review(conn, name):
    review = FetchTopReview(conn, name)
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
        html.h2(review.name),
        #html.p(review.username),
        #UserBtn(),
        html.div(
            {
                "style":{
                    "display": "flex",
                    "flexDirection": "row",
                    "justifyContent": "start",
                    "alignItems": "center"
                }
            },
            html.p(review.text),
            html.p(review.rating),
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

@component
def UserBtn(username):
    def btn_click(event):
        router.navigate(f"/user/{username}")

    return html.button(
        {"on_click": btn_click},
        f"View {username}'s Profile"
    )
    
def HomeBtn(go_home):
    return html.button(
        {"on_click": lambda event: go_home()},
        "Home"
    )

