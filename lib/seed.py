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
    
    dilemma = Song.create("Dilemma","Hip Hop",289,"Nelly",hits.id)
    complicated =  Song.create("Complicated","Rock",245,"Avril Lavigne",hits.id)
    thousand_miles = Song.create("A Thousand Miles","Pop",237,"Vanessa Carlton",hits.id)

    holiday = Song.create("Holiday","Rock",233,"Green Day",rock.id)
    dreams = Song.create("Dreams","Rock",272,"The Cranberries",rock.id)
    lullaby = Song.create("Lullaby","Rock",250, "The Cure",rock.id)

    chicken = Song.create("Chicken Fried","Country",238, "Zac Brown Band",country.id)
    green_tractor = Song.create("Big Green Tractor","Country",204, "Jason Aldean",country.id)
    alabama = Song.create("Sweet Home Alabama","Country",288, "Lynyrd Skynyrd",country.id)

    blk_and_yllw = Song.create("Black and Yellow","Hip Hop",218, "Wiz Khalifa",hip.id)
    just_a_dream = Song.create("Just a Dream","Hip Hop",238, "Nelly",hip.id)
    jackson = Song.create("Ms. Jackson","Hip Hop",271, "Outkast",hip.id)

    rock_your_body = Song.create("Rock Your Body","Pop",267, "Justin Timberlake",dance.id)
    believe = Song.create("Believe","Pop",239, "Cher",dance.id)
    blues = Song.create("Blue","Dance",284, "Eiffel 65",dance.id)


seed_database()
print("Music database seeded")