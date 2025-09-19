Movie Management System

A simple web application to manage movies, genres, and directors using Flask, SQLite, and Bootstrap.

Features:
- Add, edit, and delete movies
- Add genres and directors
- Search movies by title
- View statistics
- Simple and responsive user interface

Project Structure:
Movie-Management-System/
│
├─ app.py                 # Main Flask application
├─ storage/               # Database and storage logic
│   ├─ db_init.py         # Creates the database tables
│   ├─ seed_data.py       # Adds initial data
│   ├─ movies.db          # SQLite database
│   ├─ db_movies.py
│   ├─ db_directors.py
│   └─ db_genres.py
├─ models/                # Python classes for Movie, Genre, Director
├─ templates/             # HTML templates
└─ static/                # CSS and static files


Requirements
- Python 3.7?
- Flask
- Pandas
- Matplotlib
- Seaborn

How to Run ?
1. Make sure Python 3 is installed
2. Install required packages by running:
    pip install flask pandas matplotlib seaborn
3.  From the root folder (where app.py is), run:
    python app.py
3. Open browser at http://127.0.0.1:5000
