from datetime import datetime
from pymongo import MongoClient

from mongodb import filters as f, internal_queries as q
from utils import utilities as ut

################################ MAIN OF MONGODB ################################ 
# This main is an example of how to use mongodb module 
################################################################################# 

# Defining database
client = MongoClient("mongodb://localhost:27017/")
db = client["friends_birthdays"]
collection = db["friends_collection"]

# Execute here your query
