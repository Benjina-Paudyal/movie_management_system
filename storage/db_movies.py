import sqlite3
from models.Movie import Movie

DB_PATH = "storage/movies.db"

class Db_Movies:
    
    # --- CREATE ---
    def create_movie(self, movie:Movie):
        with sqlite3.connect(DB_PATH) as conn:
            cur = conn.cursor()
            cur.execute(
                """
                INSERT INTO movies (title, genre_id, director_id, release_date, review, watched) 
                VALUES (?,?,?,?,?,?)
                """,
                (
                    movie.title,
                    movie.genre_id,
                    movie.director_id,
                    movie.release_date,
                    movie.review,
                    int(movie.watched), # stores as 0/1
                ),
            )
            conn.commit()
    
    # --- READ ALL  movies including genre and director ---
    def get_movies(self) -> list[dict]:
        with sqlite3.connect(DB_PATH) as conn:
            cur = conn.cursor()
            cur.execute("""
                SELECT m.id, m.title, g.name AS genre, d.name AS director,
                    m.release_date, m.review, m.watched
                FROM movies m
                LEFT JOIN genres g ON m.genre_id = g.id
                LEFT JOIN directors d ON m.director_id = d.id
            """)

            movies = []
            for row in cur:
                movies.append({
                    "id": row[0],
                    "title": row[1],
                    "genre": row[2],
                    "director": row[3],
                    "release_date": row[4],
                    "review": row[5],
                    "watched": bool(row[6])
                })
            return movies
    
    # --- READ by id ---
    def get_movie_by_id(self, movie_id : int) : 
        with sqlite3.connect(DB_PATH) as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM movies WHERE id = ?", (movie_id,))
            row = cur.fetchone() # fetches one row from the result of the query , row is tuple
            if row:
                return Movie(row[0], row[1], row[2], row[3], row[4], row[5], bool(row[6])) # convert tuple to Movie object
            return None
   
   # --- READ by Name and release date ---
    def get_movie_by_title_and_release(self, title, release_date):
        with sqlite3.connect(DB_PATH) as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM movies WHERE title=? AND release_date=?", (title, release_date))
            row = cur.fetchone() 
        if row:
            return Movie(*row)
        return None
        
    # --- UPDATE ---
    def update_movie(self, movie: Movie):
        with sqlite3.connect(DB_PATH) as conn:
            cur = conn.cursor()
            cur.execute(
                """
                UPDATE movies SET title = ?, genre_id = ?, director_id = ?, release_date = ?, review = ?, watched = ? WHERE id = ?
                """,
                (
                    movie.title,
                    movie.genre_id,
                    movie.director_id,
                    movie.release_date,
                    movie.review,
                    int(movie.watched),
                    movie.id,
                ),
            )
            conn.commit()
    
    # --- DELETE ---
    def delete_movie(self, movie_id: int):
        with sqlite3.connect(DB_PATH) as conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM movies WHERE id = ?", (movie_id,))
            conn.commit()
                      
            
    # --- COUNT MOVIES ---
    def count_movies(self):
        with sqlite3.connect(DB_PATH) as conn:
            cur = conn.cursor() 
            cur.execute("SELECT COUNT(*) FROM movies")
            count = cur.fetchone()[0] 
        return count   
            
            
            
    
        

