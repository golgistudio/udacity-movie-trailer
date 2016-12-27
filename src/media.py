"""
    ToDo
"""
class Movie(object):
    """
        ToDo
    """
    title = ""
    poster_image_url = ""
    trailer_youtube_url = ""
    rating = ""
    genre = ""
    storyline = ""
    year = ""
    def __init__(self, title, thumbnail, trailer):
        self.title = title
        self.poster_image_url = thumbnail
        self.trailer_youtube_url = trailer

    def update_from_json(self, movie_info):
        """
            Todo
        """
        self.title = movie_info["title"]
        self.poster_image_url = movie_info["thumbnail"]
        self.trailer_youtube_url = movie_info["trailer"]
        self.rating = movie_info["rating"]
        self.genre = movie_info["genre"]
        self.storyline = movie_info["storyline"]
        self.year = movie_info["year"]

    def update_storyline(self, storyline):
        """
            Todo
        """
        self.storyline = storyline
