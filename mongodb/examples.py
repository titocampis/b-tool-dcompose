from datetime import datetime
from pymongo import MongoClient, ASCENDING

import filters as f
import internal_queries as q

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["friends_birthdays"]
collection = db["friends_collection"]

name = "jose antonio campos valencia"
alias = "tito"

q.insert_friend(collection, name=name, birthday=datetime(1972, 6, 1, 0, 0), sex=True, alias='Ivan', phone='000000000')
q.update_by_name(collection, name, 'sex', False)
q.update_by_name(collection, name, 'birthday', datetime(2002, 7, 8, 0, 0))
q.update_by_name(collection, name, 'phone', '605947108')
q.update_by_name(collection, name, 'alias', 'tito')
q.remove_friend_by_name(collection, "Jimena Cricketa")
f.get_friend_by_alias(collection, 'tete')
f.get_friend_by_name(collection, name)
q.get_friends(collection)
f.get_birthdays_by_month(collection, 'march')