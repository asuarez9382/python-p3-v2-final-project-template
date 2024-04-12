from models.__init__ import CONN, CURSOR
from models.playlist import Playlist

#Songs belong to playlists

class Song:
    
    all = {}
    
    def __init__(self, title, genre, duration, artist, playlist_id, id = None):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.artist = artist
        self.playlist_id = playlist_id
        self.id = id
        
    def __repr__(self):
        return f'Song ID: {self.id} Song Title: {self.title} Song genre: {self.genre} Duration: {self.duration} Artist: {self.artist} Playlist ID: {self.playlist_id}'
    
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
        genres= ['pop','dance','rock','r&b','country', 'hip hop']
        if isinstance(genre, str) and len(genre) >= 3:
            genre_lower = genre.lower()
            if genre_lower in genres:
                self._genre = genre
            else:
                raise ValueError("Genre must be pop, dance, rock, r&b, country, or hip hop")
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
     
       
    @property
    def playlist_id(self):
        return self._playlist_id
    
    @playlist_id.setter
    def playlist_id(self, playlist_id):
        if isinstance(playlist_id, int) and Playlist.find_by_id(playlist_id):
            self._playlist_id = playlist_id
        else:
            raise ValueError("Playlist_id must be an integer and must exist in the playlists table")
            
   
        
    @classmethod
    def create_table(cls):
        sql="""
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                title TEXT,
                genre TEXT,
                `duration (sec)`INTEGER,
                artist TEXT,
                playlist_id INTEGER,
                FOREIGN KEY (playlist_id) REFERENCES playlists(id)
            )
        """
        
        CURSOR.execute(sql)
        CONN.commit()
        
    @classmethod
    def drop_table(cls):
        sql="""
            DROP TABLE IF EXISTS songs
        """
        
        CURSOR.execute(sql)
        CONN.commit()
        
    @classmethod
    def instance_from_db(cls, row):
        """Creates a song object from a row in the songs table"""
        
        song = cls.all.get(row[0])
        
        if song:
            song.title = row[1]
            song.genre = row[2]
            song.duration = row[3]
            song.artist = row[4]
            song.playlist_id = row[5]
        else:
            song = cls(row[1], row[2], row[3], row[4], row[5])
            song.id = row[0]
            cls.all[song.id] = song
        return song    
        
    @classmethod
    def get_all(cls):
        sql="""
            SELECT *
            FROM songs
        """
        
        rows = CURSOR.execute(sql).fetchall()
        return [ cls.instance_from_db(row) for row in rows ]
    
    
    def save(self):
        """Inserts row into the songs table"""
        sql="""
            INSERT INTO songs(title, genre, `duration (sec)`, artist, playlist_id)
            VALUES (?, ?, ?, ?, ?)
        """
        
        CURSOR.execute(sql,(self.title, self.genre, self.duration, self.artist, self.playlist_id))
        CONN.commit()
        
        #Assigns the self.id to the id in the songs table and adds it to the all dictionary
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
        
    @classmethod
    def create(cls, title, genre, duration, artist, playlist_id):
        """Creates a song object and adds it to the songs table"""
        song = Song(title, genre, duration, artist, playlist_id)
        
        song.save()
        
        return song
    
    def update(self):
        """Updates the row in the table"""
        sql ="""
            UPDATE songs
            SET title = ?, genre = ?, `duration (sec)` = ?, artist = ?, playlist_id = ?
            WHERE id = ?
        """
        
        CURSOR.execute(sql, (self.title, self.genre, self.duration, self.artist, self.playlist_id, self.id))
        CONN.commit()
        
    def delete(self):
        sql="""
            DELETE FROM songs
            WHERE id = ?
        """
        
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        
        del type(self).all[self.id] 
        self.id = None
    
    @classmethod
    def find_by_id(cls, id):
        sql="""
            SELECT *
            FROM songs
            WHERE id = ?
        """
        
        row = CURSOR.execute(sql, (id,)).fetchone()
    
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_title(cls, title):
        sql="""
            SELECT *
            FROM songs
            WHERE title = ?
        """
        
        row = CURSOR.execute(sql, (title,)).fetchone()
        return cls.instance_from_db(row) if row else None
        
    
        