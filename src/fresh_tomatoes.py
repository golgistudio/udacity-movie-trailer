"""
  ToDo
"""

import webbrowser
import os
import re
import sys

# Styles and scripting for the page
MAIN_PAGE_HEAD = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Fresh Tomatoes!</title>
    <link rel="icon" 
      type="image/x-icon" 
      href="favicon.ico" />

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link rel="stylesheet" type="text/css" href="styles/styles.css" media="screen" />
    <link rel="stylesheet" type="text/css" href="styles/bootstrap-overrides.css" media="screen" />
</head>
<body>
'''

MAIN_PAGE_FOOTER = '''
    <script src="https://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <script src="js/actions.js" type="text/javascript" charset="utf-8"></script>
  </body>
</html>
'''

# The main page layout and title bar
MAIN_PAGE_CONTENT = '''
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24" alt="close"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-left">
            <a class="navbar-brand" href="#">
              <img src="images/noun_23947.png" alt="logo" />
              Fresh Tomatoes Movie Trailers</a>
          </div>
           <ul class="nav navbar-nav navbar-right">
              <li><a href="https://github.com/golgistudio/udacity-movie-trailer" target="_blank">Github</a></li>
           </ul>
        </div>
      </div>
    </div>
    <div class="movies">
      {movie_tiles}
    </div>
'''


# A single movie entry html template
MOVIE_TITLE_CONTENT = '''
<div class="movie-card text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <div class="movie-info">
      <div class="movie-thumbnail">
        <img src="{poster_image_url}"  alt="{movie_title}">
      </div>
      <div class="movie-description">
        <div class="movie-description-header"> 
          {movie_title}
        </div>
        <div class="movie-description-sub-header">
              {genre} 
        </div>
        <div class="movie-description-content"> 
          {storyline}
        </div>
        <div class="movie-description-footer"> 
          <span class="movie-description-footer-left">
            {rating}
          </span>
          <span class="movie-description-footer-right">
            {year}  
          </span>
        </div>
      </div>
    </div>
</div>
'''

def create_movie_tiles_content(movies):
    """
      ToDo
    """
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += MOVIE_TITLE_CONTENT.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            year=movie.year,
            storyline=movie.storyline,
            genre=movie.genre,
            rating=movie.rating
        )
    return content


def open_movies_page(movies):
    """
      ToDo
    """
    # Create or overwrite the output file
    sys.path.append("../")
    output_file = open('public/index.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = MAIN_PAGE_CONTENT.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(MAIN_PAGE_HEAD + rendered_content + MAIN_PAGE_FOOTER)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
