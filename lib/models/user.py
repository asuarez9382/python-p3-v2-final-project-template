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
        return f'User ID: {self.id} Username: {self.username} Email: {self.email} Age: {self.age}'
 
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
        
    def save(self):
        sql="""
            INSERT INTO users (username, email, age)
            VALUES (?, ?, ?)
        """  
        
        CURSOR.execute(sql, (self.username, self.email, self.age))
        CONN.commit()
        
        self.id = CURSOR.lastrowid
        
        type(self).all[self.id] = self
         
        
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
        
        #saves instance as a row to the database
        user.save()
        
        #saves newly created user instance into the class dictionary by id
        cls.all[user.id] = user
        
        return user
    
    @classmethod
    def instance_from_db(cls, row):
        """Returns the user object that is a row from the users table"""
        user = cls.all.get(row[0])
        if user:
            user.username = row[1]
            user.email = row[2]
            user.age = row[3]
        else:
            user = cls(row[1], row[2], row[3])
            user.id = row[0]
            cls.all[user.id] = user
        return user
            
    
    @classmethod
    def get_all(cls):
        sql="""
            SELECT *
            FROM users
        """
        
        users = CURSOR.execute(sql).fetchall()
        return [ cls.instance_from_db(user) for user in users ]
    
    @classmethod
    def find_by_id(cls, id):
        sql="""
            SELECT *
            FROM users
            WHERE id = ?
        """
        
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_username(cls, username):
        sql="""
            SELECT *
            FROM users
            WHERE username = ?
        """
        
        row = CURSOR.execute(sql, (username,)).fetchone()
        return cls.instance_from_db(row) if row else None
        
    
    def update(self):
        """Updates the row in the table that corresponds to the User object"""
        sql="""
            UPDATE users
            SET username = ?, email = ?, age = ?
            WHERE id = ?
        """
        
        CURSOR.execute(sql,(self.username, self.email, self.age, self.id))
        CONN.commit()

    def delete(self):
        """Deletes the row in the table that corresponds to the User ID"""
        sql="""
            DELETE FROM users
            WHERE id = ?
        """
        
        CURSOR.execute(sql,(self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None
    
    