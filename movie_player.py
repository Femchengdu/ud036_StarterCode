import fresh_tomatoes
import get_api_data

matrix_search = get_api_data.get_tmdb_object(603)

matrix_movie = get_api_data.create_movie_player_object(matrix_search)

se7en_search = get_api_data.get_tmdb_object(807)

se7en_movie = get_api_data.create_movie_player_object(se7en_search)

movies = [matrix_movie, se7en_movie]

fresh_tomatoes.open_movies_page(movies)
