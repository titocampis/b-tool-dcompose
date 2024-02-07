from datetime import datetime
from pymongo import MongoClient, ASCENDING

import queries as q

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["friends_birthdays"]
collection = db["friends_collection"]

#q.insert_friend(collection, name="mario alcaide almazan", birthday=datetime(2006, 5, 8, 0, 0), sex=True, alias='Mario', phone='685588563')

# name = "Jiminy Cricket"
# q.update_by_name(collection, name, 'sex', False)
# q.update_by_name(collection, name, 'alias', 'Jiminy')
# q.update_by_name(collection, name, 'phone', '654321987')
q.remove_friend_by_name(collection, "Jimena Cricketa")
# q.get_friend_by_alias(collection, 'tete')
#q.get_friend_by_name(collection, name)
q.get_friends(collection)

# TODO: Laura Ortiz phone