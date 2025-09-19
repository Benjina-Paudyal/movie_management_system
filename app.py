from flask import Flask,render_template, request, url_for, redirect
from models.Movie import Movie
from services.movie_service import MovieService
from services.director_service import DirectorService
from services.genre_service import GenreService

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import io
import base64

app = Flask(__name__)
movie_service = MovieService()
director_service = DirectorService()
genre_service = GenreService()

# ----------------------------------------------------------- MOVIES ----------------------------------------------------------------
@app.route("/")
def home():
    total_movies = movie_service.count_movies()
    total_directors = director_service.count_directors()
    total_genres = genre_service.count_genres()
    
    return render_template(
        'index.html',
        total_movies = total_movies,
        total_directors = total_directors,
        total_genres = total_genres
        )

@app.route("/movies")
def view_movies():
    movies = movie_service.get_movies()  
    return render_template("movies/movies.html", movies=movies)

@app.route("/movies/add", methods=["GET", "POST"])
def add_movie():
    genres = genre_service.get_genres()
    directors = director_service.get_directors()
    error_message = None

    if request.method == "POST":
        # read form data and strip whitespace
        title = request.form.get("title", "").strip()
        genre_id = request.form["genre_id"]
        director_id = request.form["director_id"]
        release_date = request.form.get("release_date", "").strip()
        review = request.form.get("review", "").strip()
        watched = "watched" in request.form 

       # basic validation
        if not title:
            error_message = "Movie title cannot be empty"
        elif not genre_id:
            error_message = "Please select a genre"
        elif not director_id:
            error_message = "Please select a director"
        elif not release_date:
            error_message = "Release date cannot be empty"
        else:
            movie_service.create_movie(title, int(genre_id), int(director_id), release_date, review, watched)
            return redirect(url_for("view_movies"))

    return render_template("movies/add_movie.html", genres=genres, directors=directors, error=error_message)


@app.route("/movies/edit/<int:movie_id>",methods=["GET", "POST"])
def edit_movie(movie_id):
    movie = movie_service.get_movie_by_id(movie_id)
    if not movie:
        return "Movie not found", 404

    genres = genre_service.get_genres()
    directors = director_service.get_directors()
    error_message = None

    if request.method == "POST":
        title=request.form.get("title", "").strip()
        genre_id=request.form.get("genre_id")
        director_id=request.form.get("director_id")
        release_date = request.form.get("release_date", "").strip()
        review = request.form.get("review", "").strip()
        watched="watched" in request.form
                
        # basic validation
        if not title:
            error_message = "Movie title cannot be empty"
        elif not genre_id:
            error_message = "Please select a genre"
        elif not director_id:
            error_message = "Please select a director"
        elif not release_date:
            error_message = "Release date cannot be empty"
        else:
            # all valid → update movie
            update_movie = Movie(
                id=movie_id,
                title=title,
                genre_id=int(genre_id),
                director_id=int(director_id),
                release_date=release_date,
                review=review,
                watched=watched
            )    
            movie_service.update_movie(update_movie)
            return redirect(url_for("view_movies"))

    return render_template(
        "movies/edit_movie.html",
        movie=movie,
        genres=genres,
        directors=directors,
        error = error_message
    )

@app.route("/movies/delete/<int:movie_id>", methods=["POST"])
def delete_movie(movie_id):
    movie_service.delete_movie(movie_id)
    return redirect(url_for("view_movies"))


# -------------------------------------------------- GENRE --------------------------------------------------------

@app.route("/genres", methods=["GET"])
def view_genres():
    genres = genre_service.get_genres()  
    return render_template("genres/genres.html", genres=genres)


@app.route("/genres/add", methods=["GET", "POST"])
def add_genre():
    error_message = None
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        if not name:
            error_message = "Genre name cannot be empty"
        elif not genre_service.create_genre(name):
            error_message = "Genre already exists!"
        else:
            return redirect(url_for("view_genres"))
    return render_template("genres/add_genre.html", error = error_message)


@app.route("/genres/<genre_name>")
def genre_movies(genre_name):
    all_movies = movie_service.get_movies() 
    movies = [m for m in all_movies if m["genre"] == genre_name]
    return render_template("genres/genre_movies.html", genre_name=genre_name, movies=movies)


# ------------------------------------- DIRECTOR ------------------------------------------------------------------------------------

@app.route("/directors", methods=["GET"])
def view_directors():
    directors = director_service.get_directors()  
    return render_template("directors/directors.html", directors=directors)


@app.route("/directors/add", methods=["GET", "POST"])
def add_director():
    error_message = None
    
    if request.method == "POST":
        name = request.form.get("name", "").strip() 
        if not name:
            error_message = "Director name cannot be empty."
        else:
            director_service.create_director(name)
            return redirect(url_for("view_directors"))
        
    return render_template("directors/add_director.html", error = error_message)


# -------------------------------------------------------------SEARCH --------------------------------------------------------------------

@app.route("/search", methods=["GET"])
def search_movies():
    query = request.args.get("query", "").strip() 
    movies = []

    if query:  
        all_movies = movie_service.get_movies()  
        # Filter movies 
        movies = [m for m in all_movies if query.lower() in m['title'].lower()]

    return render_template("movies/search_results.html", movies=movies, query=query)


# ------------------------------------------------------- STATISTICS --------------------------------------------------------------------------
@app.route("/movies/stats")
def stats():
    movies = movie_service.get_movies()
    
    # Convert to dataframe(pandas)
    df = pd.DataFrame({
    "genre": [m['genre'] for m in movies],
    "watched": [m['watched'] for m in movies]
})
# -------------------------------- Pie chart: Watched vs Unwatched-------------------------------------------------------
    plt.figure(figsize=(4,4))
    watched_counts = df['watched'].value_counts()
    
    # Plot pie chart
    watched_counts.plot.pie(
        labels=['Unwatched', 'Watched'], 
        autopct='%1.1f%%', 
        colors=['red','green']
        )
    plt.ylabel('') # hide y-axis label
    
    # Save pie chart to memory buffer as base64 for HTML
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    pie_plot = base64.b64encode(buf.getvalue()).decode()
    buf.close()
    plt.close() # close figure to free memory


# ----------------------------------------------------- Bar chart: Movies per genre-----------------------------------------
    plt.figure(figsize=(6,4))
    
    # Seaborn automatically counts number of movies per genre
    sns.countplot(x="genre", data=df, palette="pastel")
    plt.title("Movies per Genre")
    plt.xlabel("Genre")
    plt.ylabel("Number of Movies")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()  
    
    # Save bar chart to memory buffer as base64 for HTML     
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    bar_plot = base64.b64encode(buf.getvalue()).decode()
    buf.close()
    plt.close()

    return render_template("movies/stats.html", pie_plot=pie_plot, bar_plot=bar_plot)



if __name__=='__main__':
    app.run(debug=True, use_reloader=False)
    