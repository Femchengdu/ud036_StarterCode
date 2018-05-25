import tmdbsimple as tmdb
import fresh_tomatoes
import media
import env
import os

"""
The movie player creates the movie objects and then passes the list of
movies to the fresh tomatoes module
"""

# This is set in the module called env.py this file is ignored by default
# to protect secret keys
tmdb.API_KEY = os.environ['TMDB_API_KEY']

# Function to get the move object


def get_tmdb_object(movie_id):
    search = tmdb.Movies(movie_id)
    return search

# Function to make the youtube trailer link


def make_trailer_link(movie_search):
    # Youtube video base url
    base_url = 'https://www.youtube.com/watch?v='
    # Get video information
    movie_search.videos()
    # Get youtube video sub string from the result
    youtube_video_key = movie_search.results[0]['key']
    # Construct full youtube link
    youtube_video_url = base_url + youtube_video_key
    return youtube_video_url

# fuction to make the paoster link


def make_poster_links(poster_path):
    # tmdb base url
    base_url = 'http://image.tmdb.org/t/p/'
    # Poster size
    size = 'w154'
    # contruct the full link
    poster_url = base_url + size + poster_path
    return poster_url

# Set movie object attributes


def create_movie_player_object(movie_search):
    # Get the movie properties
    movie_search.info()
    # Set the movie atrributes from the movie class
    movie_player_object = media.Movie(movie_search.title,
                                      movie_search.overview,
                                      make_poster_links(
                                                       movie_search.poster_path
                                                        ),
                                      make_trailer_link(movie_search))
    return movie_player_object


# Function to create a list of movie objects from a list of tmdb ids
def create_movie_list(tmdb_movie_ids):
    tmdb_movie_list = []
    for tmdb_movie_id in tmdb_movie_ids:
        tmdb_movie_search = get_tmdb_object(tmdb_movie_id)
        tmdb_movie = create_movie_player_object(tmdb_movie_search)
        tmdb_movie_list.append(tmdb_movie)
    return tmdb_movie_list


# List of movie ids from the tmdb database
tmdb_movie_ids = [603, 807, 629]

# Create a list of tmdb movie objets
tmdb_movies = create_movie_list(tmdb_movie_ids)

# Pass the list of movie objects to the open movies
# fuction from the fresh tomatoes module
fresh_tomatoes.open_movies_page(tmdb_movies)
