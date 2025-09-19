from storage.db_movies import Db_Movies
from storage.db_directors import Db_Directors
from storage.db_genres import Db_Genres
from models.Genre import Genre

class GenreService:
    def __init__(self):
        self.__db__genres = Db_Genres()
    
    # --- create genre --
    def create_genre(self, name: str) -> bool:
        existing = self.__db__genres.get_genre_by_name(name)
        if existing:
            return False  
        new_genre = Genre(None, name)
        self.__db__genres.create_genre(new_genre)
        return True
    
    # --- get all genres ---
    def get_genres(self):
        return self.__db__genres.get_genres()
    
    # --- get genre by id ---
    def get_genre_by_id(self, genre_id : int):
        return self.__db__genres.get_genre_by_id(genre_id)
    
    # --- count genres ---
    def count_genres(self):
        return self.__db__genres.count_genres()