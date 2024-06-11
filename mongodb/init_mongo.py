import os
from pymongo import MongoClient, ASCENDING

import internal_queries as q

# Get MongoDB connection details from environment variables
mongo_host = os.getenv('MONGO_HOST', 'localhost')
mongo_port = int(os.getenv('MONGO_PORT', 27017))

# Defining database
client = MongoClient(mongo_host, mongo_port)
db = client["friends_birthdays"]
collection = db["friends_collection"]

# Set the name field as unique
collection.create_index([('name', 1)], unique=True)
# q.create_birthday_index(collection)

# Get indexes
q.get_indexes(collection)
