from models.__init__ import CURSOR, CONN

from models.user import User


def seed_database():
    """Restarts the database with the original values in all the tables"""
    
    print("Seeding the music database")
    
    User.drop_table()
    User.create_table()
    print("Created users table")
    
    User.create("mochi9382","mochi@gmail.com", 21)
    User.create("bella11","bella@gmail.com", 22)
    User.create("ozzy34","ozzy@gmail.com", 35)
    User.create("charlie92","charlie@gmail.com", 40)
    User.create("tempi22","tempi@gmail.com", 20)
    print("Finished adding users into users table")

seed_database()
print("Music database seeded")