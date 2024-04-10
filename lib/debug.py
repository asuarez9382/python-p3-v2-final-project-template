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

User.create("mochi9382","mochi@gmail.com", 21)
User.create("bella11","bella@gmail.com", 22)
User.create("ozzy34","ozzy@gmail.com", 35)
User.create("charlie92","charlie@gmail.com", 40)
User.create("tempi22","tempi@gmail.com", 20)

Song("Dilemma","Hip Hop",289,"Nelly")
Song("Complicated","Rock",245,"Avril Lavigne")
Song("A Thousand Miles","Pop",237,"Vanessa Carlton")

Song("Holiday","Rock",233,"Green Day")
Song("Dreams","Rock",272,"The Cranberries")
Song("Lullaby","Rock",250, "The Cure")

Song("Chicken Fried","Country",238, "Zac Brown Band")
Song("Big Green Tractor","Country",204, "Jason Aldean")
Song("Sweet Home Alabama","Country",288, "Lynyrd Skynyrd")

Song("Black and Yellow","Hip Hop",218, "Wiz Khalifa")
Song("Just a Dream","Hip Hop",238, "Nelly")
Song("Ms. Jackson","Hip Hop",271, "Outkast")

Song("Rock Your Body","Pop",267, "Justin Timberlake")
Song("Believe","Pop",239, "Cher")
Song("Blue","Dance",284, "Eiffel 65")

Playlist.create("Top Hits of 2002","Top songs from the year 2002",1)
Playlist.create("Rock Mix","A mix of more modern rock music",2)
Playlist.create("Country Hits Everyone Knows","Popular country songs that everyone knows",4)
Playlist.create("Hip Hop Mix","A mix of popular hip hop songs",3)
Playlist.create("Fun Dance Party Mix","Dance mix with fun songs to dance to",5)

ipdb.set_trace()
