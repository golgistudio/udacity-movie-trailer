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
    def __init__(self, title, thumbnail, trailer):
        self.title = title
        self.poster_image_url = thumbnail
        self.trailer_youtube_url = trailer

    def create_from_json(self, movie_info):
        """
            Todo
        """
        self.title = movie_info["title"]
        self.poster_image_url = movie_info["thumbnail"]
        self.trailer_youtube_url = movie_info["trailer"]

    def create_from_json2(self, movie_info):
        """
            Todo
        """
        self.title = movie_info["title"]
        self.poster_image_url = movie_info["thumbnail"]
        self.trailer_youtube_url = movie_info["trailer"]
