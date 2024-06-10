from datetime import datetime
import os
from pymongo import MongoClient

from mongodb import filters as f, internal_queries as q
from utils import utilities as ut

################################ MAIN OF MONGODB ################################ 
# This main is an example of how to use mongodb module 
################################################################################# 

# Get MongoDB connection details from environment variables
mongo_host = os.getenv('MONGO_HOST', 'localhost')
mongo_port = int(os.getenv('MONGO_PORT', 27017))

# Defining database
client = MongoClient(mongo_host, mongo_port)
db = client["friends_birthdays"]
collection = db["friends_collection"]

# Execute here your query
