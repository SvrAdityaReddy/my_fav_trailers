import webbrowser
class Movie():
    """This class holds information regarding movies"""
    VALID_RATINGS=["G","PG","PG-13","R"]; #CLASS VARIABLE
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_link):
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer=trailer_link
    def show_tailer(self):
        webbrowser.open(self.trailer,new=1,autoraise=True);