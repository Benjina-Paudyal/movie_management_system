from storage.db_movies import Db_Movies
from storage.db_directors import Db_Directors
from storage.db_genres import Db_Genres
from models.Movie import Movie

class MovieService:
    def __init__(self):
        self.__db_movies = Db_Movies()
        self.__db_directors = Db_Directors()
        self.__db_genres = Db_Genres()
    
    # -- create movie ---
    def create_movie(self, title, genre_id, director_id, release_date, review, watched):
        new_movie = Movie(None, title, genre_id, director_id, release_date, review, watched)
        self.__db_movies.create_movie(new_movie)
        
    # -- get all movies ---
    def get_movies(self):
        return self.__db_movies.get_movies()
    
    # -- get movie by id ---
    def get_movie_by_id(self, movie_id: int):
        return self.__db_movies.get_movie_by_id(movie_id)
    
    # -- update movie  --
    def update_movie(self, updated_movie: Movie):
        self.__db_movies.update_movie(updated_movie)
        return self.get_movie_by_id(updated_movie.id)
    
    # -- delete movie --
    def delete_movie(self, movie_id: int):
        self.__db_movies.delete_movie(movie_id)
    
    # --- count movies ---
    def count_movies(self):
        return self.__db_movies.count_movies()
    
    
    
        
