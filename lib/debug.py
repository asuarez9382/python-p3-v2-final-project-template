#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CURSOR, CONN
import ipdb

from models.user import User

mochi = User("mochi11","mochi@gmail.com", 21)

User.create("mochi9382","mochi@gmail.com", 21)


ipdb.set_trace()
