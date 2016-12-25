"""
list of movies that feed into fresh_tomatoes.py file
"""
import json
import fresh_tomatoes
import media

MOVIE_LIST = []
with open("data/movies.json") as json_file:
    JSON_DATA = json.load(json_file)
    for key in JSON_DATA:
        value = JSON_DATA[key]
        movie_item = media.Movie(value["title"],
                                 value["thumbnail"],
                                 value["trailer"])
        MOVIE_LIST.append(movie_item)

fresh_tomatoes.open_movies_page(MOVIE_LIST)
