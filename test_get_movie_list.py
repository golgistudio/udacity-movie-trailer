"""
    ToDo
"""

import unittest

from get_movie_list import get_movie_list


class TestGetMovieList(unittest.TestCase):
    """
        ToDo
    """

    def test_ittle(self):
        """
            ToDo
        """
        file_name = "./tests/testData/testMovies.json"
        movie_list = get_movie_list(file_name)
        self.assertEqual(movie_list[0].title, 'Hacksaw Ridge')

if __name__ == '__main__':
    unittest.main()
