from models.__init__ import CONN, CURSOR

class Song:
    
    all = {}
    
    def __init__(self, title, genre, duration, artist, id = None, playlistID = None):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.artist = artist
        self.playlistID = playlistID
        self.id = id
        
    def __repr__(self):
        return f'Song ID: {self.id} Song Title: {self.title} Song genre: {self.genre} Duration: {self.duration} Artist: {self.artist}'
    
    @property
    def title(self):
        return self._title 
    
    @title.setter
    def title(self, title):
        if isinstance(title, str):
            self._title = title
        else:
            raise ValueError("Invalid song title. Song title must be a string.")
        
    @property
    def genre(self):
        return self._genre
    
    @genre.setter
    def genre(self, genre):
        genres= ['pop','dance','rock','r&b','country']
        if isinstance(genre, str) and len(genre) >= 3:
            genre_lower = genre.lower()
            if genre_lower in genres:
                self._genre = genre
            else:
                raise ValueError("Genre must be pop, dance, rock, r&b, country")
        else:
            raise ValueError("Genre must be a string and length must be greater than or equal to 3")
        
    @property
    def duration(self):
        return self._duration
    
    @duration.setter
    def duration(self, duration):
        if isinstance(duration, int) and duration >= 1:
            self._duration = duration
        else:
            raise ValueError("Duration must be an integer and greater than or equal to 1")
        
    @property
    def artist(self):
        return self._artist
    
    @artist.setter
    def artist(self, artist):
        if isinstance(artist, str) and len(artist) >= 1:
            self._artist = artist
        else:
            raise ValueError("Artist must be a string and greater than or equal to 1")
        
    @classmethod
    def create_table(cls):
        sql="""
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                title TEXT,
                genre TEXT,
                duration INTEGER,
                artist TEXT,
                playlist_id INTEGER,
                FOREIGN KEY (playlist_id) REFERENCES playlists(id)
            )
        """
        
        CURSOR.execute(sql)
        CONN.commit()
        