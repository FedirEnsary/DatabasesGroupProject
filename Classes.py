from reactpy import html

class movie:
    def __init__(self, name, description, rating, criticscore, genre, director, releasedate):
        self.name = name
        self.description = description
        self.rating = rating
        self.criticscore = criticscore
        self.genre = genre
        self.director = director
        self.releasedate = releasedate

    def toHtml(self):
        return html.details(
        html.summary(self.name + "(" + str(self.releasedate) + ")"),
        html.p(self.description),
        html.p("Rating: " + str(self.rating) + "    Critic Score: " + str(self.criticscore)),
        html.p("Directed by " + self.director),
        html.button()
        )


class topReview:
    def __init__(self, text, rating, title, name):
        self.name = name
        self.text = text
        self.rating = rating
        self.title = title
    
    def toHtml(self):
        print("finish me")

class review:
    def __init__(self, username, text, rating, title):
        self.username = username
        self.text = text
        self.rating = rating
        self.title = title
    
    def toHtml(self):
        print("finish me")

class user:
    def __init__(self, username, email = ""):
        self.username = username
        self.email = email