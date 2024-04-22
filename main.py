from datetime import datetime
from pymongo import MongoClient

import json
import matplotlib.pyplot as plt
from mongodb import filters as mongodb_f
from horoscope import horoscope_study as hs

# Defining database
client = MongoClient("mongodb://localhost:27017/")
db = client["friends_birthdays"]
collection = db["friends_collection"]

# Loading the json
with open('horoscope/horoscopes.json', 'r') as file:
    horoscopes_dict = json.load(file)

# Converting simple dates on datetimes
for horoscope in horoscopes_dict.values():
    horoscope['start'] = hs.date2datetime(horoscope['start'])
    horoscope['end'] = hs.date2datetime(horoscope['end'])

print(horoscopes_dict)
