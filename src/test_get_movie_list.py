"""
    Example unit test
"""

import unittest

from get_movie_list import get_movie_list


class TestGetMovieList(unittest.TestCase):
    """
        Example unit test
    """

    def test_title(self):
        """
            Verify that reading in an example json file will
            result in the expected title
        """
        file_name = "./src/tests/testData/testMovies.json"
        movie_list = get_movie_list(file_name)
        self.assertEqual(movie_list[0].title, 'The Lobster')

if __name__ == '__main__':
    unittest.main()
