from storage.db_movies import Db_Movies
from storage.db_directors import Db_Directors
from storage.db_genres import Db_Genres
from models.Movie import Movie
from models.Director import Director
from models.Genre import Genre

def seed_genres():
    db_genres = Db_Genres()
    genres = [
        Genre(None, "Action"),
        Genre(None, "Crime"),
        Genre(None, "Comedy"),
        Genre(None, "Drama"),
        Genre(None, "Horror")
    ]
    for genre in genres:
        if not db_genres.get_genre_by_name(genre.name):
            db_genres.create_genre(genre)
    print("Genres seeded.")

def seed_directors():
    db_directors = Db_Directors()
    directors = [
        Director(None, "Christopher Nolan"),
        Director(None, "David Finche"),
        Director(None, "Roman Polanski"),
        Director(None, "James Wan"),
        Director(None, "Steven Spielberg")
    ]
    for director in directors:
        if not db_directors.get_director_by_name(director.name):
            db_directors.create_director(director)
    print("Directors seeded.")
    
def seed_movies():
    db_movies = Db_Movies()
    movies = [
    Movie(None, "Movie A", 1, 1, "2010-07-16", "Mind-bending thriller", True),      
    Movie(None, "Movie B", 1, 1, "2008-07-18", "Superhero masterpiece", True),
    Movie(None, "Movie C", 2, 2, "1995-09-22", "Dark crime thriller", True),            
    Movie(None, "Movie D", 2, 3, "2007-03-02", "Investigative crime drama", False),   
    Movie(None, "Movie E", 3, 2, "1974-04-20", "Classic crime drama", True),
    Movie(None, "Movie F", 3, 2, "2010-04-01", "Supernatural horror", False), 
    Movie(None, "Movie G", 4, 4, "2010-04-01", "Historical drama", False), 
    Movie(None, "Movie H", 4, 5, "2010-04-01","Action crime drama", False), 
    Movie(None, "Movie I", 5, 4, "2010-04-01", "Very interesting", False), 
    Movie(None, "Movie J", 5, 5, "2010-04-01", "Supernatural horror", False)
    ]
    
    for movie in movies:
        if not db_movies.get_movie_by_title_and_release(movie.title, movie.release_date):
            db_movies.create_movie(movie)
    print("Movies seeded.")


if __name__ == "__main__":
    seed_genres()
    seed_directors()
    seed_movies()
    print("All data seeded successfully.")

 