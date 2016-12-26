"""
  ToDo
"""

import json
import media

def get_movie_list(file_path):
    """
        ToDo
    """
    movie_list = []
    with open(file_path) as json_file:
        json_data = json.load(json_file)
        for key in json_data:
            value = json_data[key]
            movie_item = media.Movie(value["title"],
                                     value["thumbnail"],
                                     value["trailer"])
            movie_list.append(movie_item)
    return movie_list
