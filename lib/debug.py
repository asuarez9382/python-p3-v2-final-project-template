#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CURSOR, CONN
import ipdb

from models.user import User
from models.song import Song
from models.playlist import Playlist
from helpers import list_users, update_user



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

test =Song("Dilemma","Hip Hop",289,"Nelly",hits.id)
Song("Complicated","Rock",245,"Avril Lavigne",hits.id)
Song("A Thousand Miles","Pop",237,"Vanessa Carlton",hits.id)

Song("Holiday","Rock",233,"Green Day",rock.id)
Song("Dreams","Rock",272,"The Cranberries",rock.id)
Song("Lullaby","Rock",250, "The Cure",rock.id)

Song("Chicken Fried","Country",238, "Zac Brown Band",country.id)
Song("Big Green Tractor","Country",204, "Jason Aldean",country.id)
Song("Sweet Home Alabama","Country",288, "Lynyrd Skynyrd",country.id)

Song("Black and Yellow","Hip Hop",218, "Wiz Khalifa",hip.id)
Song("Just a Dream","Hip Hop",238, "Nelly",hip.id)
Song("Ms. Jackson","Hip Hop",271, "Outkast",hip.id)

Song("Rock Your Body","Pop",267, "Justin Timberlake",dance.id)
Song("Believe","Pop",239, "Cher",dance.id)
Song("Blue","Dance",284, "Eiffel 65",dance.id)



ipdb.set_trace()
