from reactpy import component, html
from Frontend.movie import HomeBtn, UpvoteBtn, DownvoteBtn


@component
def UserProfile(username, reviews, go_home, go_to_movie):
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
            username
        ),
        [
            UserReviewEntry(review=r, go_to_movie=go_to_movie)
            for r in reviews
        ]
        
    )
    
@component
def Review(review, go_to_movie):
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
            html.h2(review.title),
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
            html.p(review.text),
            UpvoteBtn(),
            DownvoteBtn()
        )
    )