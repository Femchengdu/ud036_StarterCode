# Trying it with TMDB simple


import tmdbsimple as tmdb
import urllib2
import webbrowser
import movie

tmdb.API_KEY = '1cd7238da5972f9cf532eeeb3705ccfb' # tmdb key
YVBURL = 'https://www.youtube.com/watch?v=' # Youtube video base url
 # Search for the movie matrix by the tmdb ID (Hard coded for testing)

# Function to get the move object
def get_tmdb_object(movie_id):
	search = tmdb.Movies(movie_id)
	return search


def make_trailer_link(movie_search, YVBURL):
	movie_search.videos()
	youtube_video_key = movie_search.results[0]['key']
	youtube_video_url = YVBURL + youtube_video_key
	return youtube_video_url

def make_poster_links(poster_path):
	base_url = 'http://image.tmdb.org/t/p/'
	size = 'w154'
	poster_url = base_url + size + poster_path
	return poster_url

# Set movie object attributes
def create_movie_player_object(movie_search):
	movie_search.info() # Get the movie properties
	movie_player_object = movie.Movie(movie_search.title, movie_search.overview, make_poster_links(movie_search.poster_path), make_trailer_link(movie_search, YVBURL) )
	return movie_player_object

