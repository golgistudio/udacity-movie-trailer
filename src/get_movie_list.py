"""
    Read in the movies
"""

import json
import media

def get_movie_list(file_path):
    """
       Given a file path, parse the json and return an array of movies

       Args:
        file_path (string): Full file path for the json file

      Returns:
        movies (array of Movie) : An array of movie information.
    """
    movie_list = []
    with open(file_path) as json_file:
        json_data = json.load(json_file)
        for key in json_data:
            value = json_data[key]
            movie_item = media.Movie(value["title"],
                                     value["thumbnail"],
                                     value["trailer"])
            movie_item.update_from_json(value)
            movie_list.append(movie_item)
    return movie_list
