"""
    Movie class
"""
class Movie(object):
    """
        Definition for a movie card
    """
    title = ""
    poster_image_url = ""
    trailer_youtube_url = ""
    rating = ""
    genre = ""
    storyline = ""
    year = ""
    def __init__(self, title, thumbnail, trailer):
        """
            Constructor
        """
        self.title = title
        self.poster_image_url = thumbnail
        self.trailer_youtube_url = trailer

    def update_from_json(self, movie_info):
        """
            Retrieve from a json object more fields.abs

            Args:
                movie_info (object): json object of movie information
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
            Separate method to update a storyline

            Args:
                storyLine (string): Updated storyline to store in the instance.
        """
        self.storyline = storyline
