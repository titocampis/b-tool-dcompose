from datetime import datetime
from pymongo import MongoClient, ASCENDING

import filters as f
import internal_queries as q

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["friends_birthdays"]
collection = db["friends_collection"]

#q.insert_friend(collection, name="mario alcaide almazan", birthday=datetime(2006, 5, 8, 0, 0), sex=True, alias='Mario', phone='685588563')

name = "yolanda almazan perez"
# q.update_by_name(collection, name, 'sex', False)
q.update_by_name(collection, name, 'birthday', datetime(1995, 2, 15, 0, 0))
# q.update_by_name(collection, name, 'phone', '654321987')
# q.remove_friend_by_name(collection, "Jimena Cricketa")
# f.get_friend_by_alias(collection, 'tete')
# f.get_friend_by_name(collection, name)
q.get_friends(collection)

# TODO: Laura Ortiz phone