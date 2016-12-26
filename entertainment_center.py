"""
list of movies that feed into fresh_tomatoes.py file
"""
import fresh_tomatoes
from get_movie_list import get_movie_list

def main():
    """
        ToDo
    """
    movie_list = get_movie_list("data/movies.json")
    fresh_tomatoes.open_movies_page(movie_list)

main()
