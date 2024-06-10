from datetime import datetime
import os
from pymongo import MongoClient, ASCENDING

import filters as f
import internal_queries as q

# Get MongoDB connection details from environment variables
mongo_host = os.getenv('MONGO_HOST', 'localhost')
mongo_port = int(os.getenv('MONGO_PORT', 27017))

# Defining database
client = MongoClient(mongo_host, mongo_port)
db = client["friends_birthdays"]
collection = db["friends_collection"]

# INSERTS AND UPDATES
q.insert_friend(collection, 'mar estanyol zabala', birthday=datetime(1972, 6, 1, 0, 0), sex=True, alias='Ivan', phone='000000000')
q.insert_friend_dict(collection, {'name': 'Mar Estanyol Zabala', 'birthday': datetime(1997, 3, 17, 0, 0), 'sex': False, 'alias': 'Marseta', 'phone': '637249346', 'month': 'march', 'day': 17, 'month_number': 3})
q.update_by_name(collection, 'mar estanyol zabala', 'sex', False)
q.update_by_name(collection, 'mar estanyol zabala', 'birthday', datetime(2002, 7, 8, 0, 0))
q.update_by_name(collection, 'mar estanyol zabala', 'phone', '605947108')
q.update_by_name(collection, 'mar estanyol zabala', 'alias', 'tito')
q.remove_friend_by_name(collection, "Jimena Cricketa")

# GETTERS
print(f.get_friend_by_alias(collection, 'tete'))
print(f.get_friend_by_name(collection, 'mar estanyol zabala'))
print(f.get_friends(collection))
print(f.get_birthdays_by_month(collection, 'march'))
