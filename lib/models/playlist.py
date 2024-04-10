from models.__init__ import CONN, CURSOR
from models.user import User

#A playlist can only belong to one user

class Playlist:
    
    all = {}
    
    def __init__(self, title, description, user_id, id = None):
        self.title = title
        self.description = description
        self.id = id
        self.user_id = user_id
        
    def __repr__(self):
        return f'Playlist ID: {self.id} Playlist title: {self.title} Playlist description: {self.description} UserID: {self.user_id}'
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title) > 0:
            self._title = title
        else:
            raise ValueError("Title must be a string and have a length > 0")
        
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, description):
        if isinstance(description, str) and len(description) > 0:
            self._description = description
        else:
            raise ValueError("Description must be a string and have a length > 0")
        
    @property
    def user_id(self):
        return self._user_id
    
    @user_id.setter
    def user_id(self, user_id):
        if isinstance(user_id, int) and User.find_by_id(user_id):
            self._user_id = user_id
        else:
            raise ValueError("user_id must be an integer and must exist in users table")
        
        
    @classmethod
    def create_table(cls):
        sql="""
            CREATE TABLE IF NOT EXISTS playlists(
                id INTEGER PRIMARY KEY,
                title TEXT,
                description TEXT,
                user_id INTEGER,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        """
        
        CURSOR.execute(sql)
        CONN.commit()
        
    @classmethod
    def drop_table(cls):
        sql="""
            DROP TABLE IF EXISTS playlists
        """
        
        CURSOR.execute(sql)
        CONN.commit()
        
    def save(self):
        sql="""
            INSERT INTO playlists (title, description, user_id)
            VALUES (?,?,?)
        """
        
        CURSOR.execute(sql, (self.title, self.description, self.user_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
        
    @classmethod    
    def create(cls, title, description ,user_id):
        playlist = cls(title, description, user_id)
        
        playlist.save()
        
        return playlist
    
    @classmethod
    def instance_from_db(cls, row):
        #implement logic here
        pass
    
    @classmethod
    def find_by_id(cls, id):
        sql="""
            SELECT * 
            FROM playlists
            WHERE id = ?
        """
        
        row = CURSOR.execute(sql, (id,)).fetchone()
        
        #Add instance_to_db function
        found_playlist = Playlist(row[1],row[2],row[3])
        found_playlist.id = row[0]
        
        return found_playlist
        
        
        