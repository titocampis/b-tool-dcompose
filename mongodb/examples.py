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
q.insert_friend(collection, 'jiminy cricket gepeto', birthday=datetime(1950, 1, 1, 0, 0), sex=True, alias='pinocho', phone='123456789')
q.insert_friend_dict(collection, {'name': 'jiminy cricket gepeto', 'birthday': datetime(1950, 1, 1, 0, 0), 'sex': False, 'alias': 'pinocho', 'phone': '123456789', 'month': 'january', 'day': 1, 'month_number': 1})
q.update_by_name(collection, 'jiminy cricket gepeto', 'sex', False)
q.update_by_name(collection, 'jiminy cricket gepeto', 'birthday', datetime(1950, 1, 1, 0, 0))
q.update_by_name(collection, 'jiminy cricket gepeto', 'phone', '123456789')
q.update_by_name(collection, 'jiminy cricket gepeto', 'alias', 'pinocho')
q.remove_friend_by_name(collection, "Jimena Cricketa")

# GETTERS
print(f.get_friend_by_alias(collection, 'pinocho'))
print(f.get_friend_by_name(collection, 'jiminy cricket gepeto'))
print(f.get_friends(collection))
print(f.get_birthdays_by_month(collection, 'january'))
