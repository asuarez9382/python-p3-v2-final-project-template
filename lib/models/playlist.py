from models.__init__ import CONN, CURSOR


class Playlist:
    
    all = {}
    
    def __init__(self, title, description, id = None, user_id = None):
        self.title = title
        self.description = description
        self.id = id
        self.user_id = user_id
        
    def __repr__(self):
        return f'Playlist ID: {self.id} Playlist title: {self.title} Playlist description: {self.description}'
    
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
        