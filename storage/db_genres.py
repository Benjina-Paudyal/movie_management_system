import sqlite3
from models.Genre import Genre

DB_PATH = "storage/movies.db"

class Db_Genres:
        
    # --- CREATE ---
    def create_genre(self, genre:Genre):
        with sqlite3.connect(DB_PATH) as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO genres (name) VALUES (?)", (genre.name,))
            conn.commit()
        
    # --- READ ---
    def get_genres(self)-> list[Genre]:
        genres = []
        with sqlite3.connect(DB_PATH) as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM genres")
            for row in cur:
                genre_obj = Genre(*row) # unpacks tuple elements into the constructor parameters
                genres.append(genre_obj)
        return genres
    
    # --- READ by id ---
    def get_genre_by_id(self, genre_id:int):
       with sqlite3.connect(DB_PATH) as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM genres WHERE id = ?",(genre_id,))
            row = cur.fetchone() # fetch only the first matching row as a tuple
            if row:
                return Genre(*row)
            return None
    
    # --- READ by name ---
    def get_genre_by_name(self, name: str):
        with sqlite3.connect(DB_PATH) as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM genres WHERE name = ?", (name,))
            row = cur.fetchone()
            if row:
                return Genre(*row)
        return None

        
    # --- COUNT GENRES ---
    def count_genres(self):
        with sqlite3.connect(DB_PATH) as conn:
            cur = conn.cursor()
            cur.execute("SELECT COUNT(*) FROM genres") # counts all rows in the genres table
            count = cur.fetchone()[0] # returns a tuple
        return count   
               
        