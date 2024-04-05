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
        return f'User {self.id}: {self.username} {self.email} {self.age}'
 
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and len(username) > 0:
            self._username = username
        else:
            raise ValueError("Invalid username. Username must be a string.")
        
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        import re 
        email_pattern = r'^\S+@\S+\.\S+$'
        if isinstance(email, str) and re.match(email_pattern, email) is not None:
            self._email = email
        else:
            raise ValueError("Invalid email")
    
#Testing
mochi = User("mochi9382","mochi@gmail.com",21)

print(mochi.__repr__())