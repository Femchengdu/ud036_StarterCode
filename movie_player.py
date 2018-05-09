import fresh_tomatoes
import get_api_data

""" The movie player creates the movie objects and then passes the list of movies to the fresh tomatoes module """


# Function to create a list of movie objects from a list of tmdb ids

def create_movie_list(tmdb_movie_ids):
	tmdb_movie_list = []
	for tmdb_movie_id in tmdb_movie_ids:
		tmdb_movie_search = get_api_data.get_tmdb_object(tmdb_movie_id)
		tmdb_movie = get_api_data.create_movie_player_object(tmdb_movie_search)
		tmdb_movie_list.append(tmdb_movie)
	return tmdb_movie_list


# List of movie ids from the tmdb database
tmdb_movie_ids = [603, 807, 629]

# Create a list of tmdb movie objets
tmdb_movies = create_movie_list(tmdb_movie_ids)

# Pass the list of movie objects to the open movies fuction from the fresh tomatoes module
fresh_tomatoes.open_movies_page(tmdb_movies)
