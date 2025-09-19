class Movie:
    def __init__(self, id, title, genre_id, director_id, release_date, review, watched):
        self.__id = id
        self.__title = title
        self.__genre_id = genre_id
        self.__director_id = director_id
        self.__release_date = release_date
        self.__review = review
        self.__watched = watched
        
# ---  GETTERS & SETTERS ---
    @property
    def id(self):
        return self.__id
    
    @property
    def genre_id(self):
        return self.__genre_id

    @property
    def director_id(self):
        return self.__director_id

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_title):
        if new_title:
            self.__title = new_title
        else:
            raise ValueError("Title cannot be empty.")
        
    @property
    def release_date(self):
        return self.__release_date
    
    @release_date.setter
    def release_date(self, new_release_date):
        self.__release_date = new_release_date

    @property
    def review(self):
        return self.__review

    @review.setter
    def review(self, new_review):
        self.__review = new_review

    @property
    def watched(self):
        return self.__watched

    @watched.setter
    def watched(self, value):
        if isinstance(value, bool):
            self.__watched = value
        else:
            raise ValueError("Watched must be True or False")

# --- CONVERT TO JSON ---

    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "genre_id": self.genre_id,
            "director_id": self.director_id,
            "release_date": self.release_date,
            "review": self.review,
            "watched": self.watched,
        }
