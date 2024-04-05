from models.__init__ import CURSOR, CONN

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
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if isinstance(age, int) and age >= 5:
            self._age = age
        else:
            raise ValueError("Age must be an integer and greater than or equal to 5")
        
        
    @classmethod
    def create_table(cls):
        """ Creates a new table to save the attributes of User instances"""
        sql="""
            CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            username TEXT,
            email TEXT,
            age INTEGER
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    @classmethod
    def drop_table(cls):
        """Deletes the table from the database"""
        sql="""
            Drop TABLE IF EXISTS users
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    @classmethod
    def create(cls, username, email, age):
        #Create user instance
        user = cls(username, email, age)
        sql = """
            INSERT INTO users (username, email, age)
            VALUES (?, ?, ?)
        """
        
        #Inserts the user instance into the database
        CURSOR.execute(sql, (username, email, age))
        CONN.commit()
        
        #Gets the id for the user and saves it in the user instance
        user.id = CURSOR.lastrowid
        
        #saves newly created user instance into the class dictionary by id
        cls.all[user.id] = user
        return user
    
