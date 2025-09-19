import sqlite3

DB_NAME = "movies.db"

def create_tables():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("PRAGMA foreign_keys = ON") # To enforce foreign key rules as SQLite doesn't enforce them by default
        cur = conn.cursor()
        
        # --- GENRES TABLE ---
        cur.execute("""
        CREATE TABLE IF NOT EXISTS genres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
        """)
        
        # --- DIRECTORS TABLE ---
        cur.execute("""
        CREATE TABLE IF NOT EXISTS directors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
        """)
        
        # --- MOVIES TABLE ---
        cur.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            genre_id INTEGER,
            director_id INTEGER,
            release_date TEXT,
            review TEXT,
            watched BOOLEAN DEFAULT 0,
            FOREIGN KEY (genre_id) REFERENCES genres(id),
            FOREIGN KEY (director_id) REFERENCES directors(id)
        )
        """)
        
        conn.commit()
        print("Tables created successfully.")
        
if __name__ == "__main__":
    create_tables()
