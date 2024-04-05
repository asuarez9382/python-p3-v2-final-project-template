#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CURSOR, CONN
import ipdb

from models.user import User

mochi = User("mochi11","mochi@gmail.com", 21)

User.drop_table()
User.create_table()

User.create("mochi9382","mochi@gmail.com", 21)
User.create("bella11","bella@gmail.com", 22)
User.create("ozzy34","ozzy@gmail.com", 35)
User.create("charlie92","charlie@gmail.com", 40)
User.create("tempi22","tempi@gmail.com", 20)


ipdb.set_trace()
