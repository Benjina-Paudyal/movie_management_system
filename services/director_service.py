from storage.db_movies import Db_Movies
from storage.db_directors import Db_Directors
from storage.db_genres import Db_Genres
from models.Director import Director

class DirectorService:
    def __init__(self):
        self.__db__directors = Db_Directors()
    
    # --- create director --
    def create_director(self, name):
        new_director = Director(None, name)
        self.__db__directors.create_director(new_director)
    
    # --- get all directors ---
    def get_directors(self):
        return self.__db__directors.get_directors()
    
    # --- get director by id ---
    def get_director_by_id(self, director_id : int):
        return self.__db__directors.get_director_by_id(director_id)
            
    # --- count director ---
    def count_directors(self):
        return self.__db__directors.count_directors()
