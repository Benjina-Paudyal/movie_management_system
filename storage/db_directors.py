import sqlite3
from models.Director import Director

DB_PATH = "storage/movies.db"

class Db_Directors:
            
    # --- CREATE ---
    def create_director(self, director: Director):
        with sqlite3.connect(DB_PATH) as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO directors (name) VALUES (?)", (director.name,))
            conn.commit()
                
    # --- READ ALL ---
    def get_directors(self) -> list[Director]:
        with sqlite3.connect(DB_PATH) as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM directors")
            directors = []
            for row in cur:
                director_obj = Director(*row) # unpacks tuple elements into the constructor parameters
                directors.append(director_obj)
        return directors
    
    # ---READ by id ---
    def get_director_by_id(self, director_id: int):
        with sqlite3.connect(DB_PATH) as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM directors WHERE id = ?", (director_id,))
            row = cur.fetchone()
            if row:
                return Director(*row)
        return None
    
    # --- READ by NAME ---
    def get_director_by_name(self, name: str):
        with sqlite3.connect(DB_PATH) as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM directors WHERE name = ?", (name,))
            row = cur.fetchone()
            if row:
                return Director(*row)
        return None
        
    # --- COUNT DIRECTORS ---
    def count_directors(self):
        with sqlite3.connect(DB_PATH) as conn:
            cur = conn.cursor()
            cur.execute("SELECT COUNT(*) FROM directors")
            count = cur.fetchone()[0] 
        return count      
           
        
   