from datetime import datetime
from pymongo import MongoClient, ASCENDING

import filters as f
import internal_queries as q

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["friends_birthdays"]
collection = db["friends_collection"]

name = "helena valles teixido"
f.get_birthdays_by_month(collection, 'march')
#q.update_by_name(collection, name, 'birthday', datetime(1998, 3, 2, 0, 0))
