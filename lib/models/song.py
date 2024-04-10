from __init__ import CONN, CURSOR

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
    
    