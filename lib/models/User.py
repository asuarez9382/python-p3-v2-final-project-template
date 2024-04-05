from __init__ import CURSOR, CONN

class User:
    
    #Dictionary of objects saved to the database
    all ={}
    
    def __init__(self, username, email, age, id = None):
        self.id = id
        self.username = username
        self.email = email
        self.age = age
        
    def __repr__(self):
        return f'User {self.id}: {self.name} {self.email} {self.age}'