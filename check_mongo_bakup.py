from pymongo import MongoClient

from mongodb import filters as f, internal_queries as q

################################ MAIN OF MONGODB ################################ 
# This main is an example of how to use mongodb module 
################################################################################# 

# Defining database
client = MongoClient("mongodb://localhost:27017/")
db = client["friends_birthdays"]
collection = db["friends_collection"]

# Execute here your query
for friend in f.get_friends(collection):
    print(friend)
