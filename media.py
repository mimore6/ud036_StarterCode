import webbrowser

# Define Movie Class
class Movie():
    # The Movie() lets you create instance of movie with its information

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """create movie constructor with pertinent
            information given when you create class"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
