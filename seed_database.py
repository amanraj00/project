"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb positivity')
os.system('createdb positivtiy')

model.connect_to_db(server.app)
model.db.create_all()