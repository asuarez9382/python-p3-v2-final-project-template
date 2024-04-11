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
        """Creates a table"""
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
        """Deletes the table"""
        sql="""
            DROP TABLE IF EXISTS playlists
        """
        
        CURSOR.execute(sql)
        CONN.commit()
        
    def save(self):
        """Adds a new row to the playlists table"""
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
        """Creates a new playlist object and adds it to both the table and the all dictionary"""
        playlist = cls(title, description, user_id)
        
        playlist.save()
        
        return playlist
    
    @classmethod
    def instance_from_db(cls, row):
        """Turns a row in the table to a playlist object"""
        playlist = cls.all.get(row[0])
        
        if playlist:
            playlist.title = row[1]
            playlist.description = row[2]
            playlist.user_id = row[3]
        else:
            playlist = cls(row[1],row[2],row[3])
            playlist.id = row[0]
            cls.all[playlist.id] = playlist
        return playlist
    
    @classmethod
    def find_by_id(cls, id):
        """Finds the row in the playlists table that corresponds with the id inputed and returns the row and a playlist object"""
        sql="""
            SELECT * 
            FROM playlists
            WHERE id = ?
        """
        
        row = CURSOR.execute(sql, (id,)).fetchone()
        
        found_playlist = cls.instance_from_db(row) if row else None
        
        return found_playlist
        
    @classmethod
    def get_all(cls):
        """Returns all the rows from the playlist table as playlist objects"""
        sql="""
            SELECT *
            FROM playlists
        """
        
        rows = CURSOR.execute(sql).fetchall()
        return [ cls.instance_from_db(row) for row in rows ]
    
    def update(self):
        """Updates the row in the playlists table that corresponds to the playlist object id"""
        sql="""
            UPDATE playlists
            SET title = ?, description = ?, user_id = ?
            WHERE id = ?
        """
        
        CURSOR.execute(sql, (self.title, self.description, self.user_id, self.id))
        CONN.commit()
        
    def delete(self):
        """
            Deletes the row in the playlist table and deletes the object in the Playlist.all dictionary.
            Also sets the corresponding id in the all dictionary to None
        """
        sql="""
            DELETE FROM playlists
            WHERE id = ?
        """
        
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        
        del type(self).all[self.id]
        self.id = None