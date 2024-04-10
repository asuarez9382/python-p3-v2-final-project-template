from models.__init__ import CURSOR, CONN

from models.user import User
from models.playlist import Playlist
from models.song import Song


def seed_database():
    """Restarts the database with the original values in all the tables"""
    
    print("Seeding the music database")
    
    User.drop_table()
    Song.drop_table()
    Playlist.drop_table()

    User.create_table()
    Song.create_table()
    Playlist.create_table()

    mochi = User.create("mochi9382","mochi@gmail.com", 21)
    bella = User.create("bella11","bella@gmail.com", 22)
    ozzy = User.create("ozzy34","ozzy@gmail.com", 35)
    charlie = User.create("charlie92","charlie@gmail.com", 40)
    tempi = User.create("tempi22","tempi@gmail.com", 20)

    hits = Playlist.create("Top Hits of 2002","Top songs from the year 2002",mochi.id)
    rock = Playlist.create("Rock Mix","A mix of more modern rock music",bella.id)
    country = Playlist.create("Country Hits Everyone Knows","Popular country songs that everyone knows",mochi.id)
    hip = Playlist.create("Hip Hop Mix","A mix of popular hip hop songs",tempi.id)
    dance = Playlist.create("Fun Dance Party Mix","Dance mix with fun songs to dance to",charlie.id)
    


seed_database()
print("Music database seeded")