# from datetime import datetime
# from pymongo import MongoClient, ASCENDING

# import filters as f
# import internal_queries as q

# # Connect to MongoDB
# client = MongoClient("mongodb://localhost:27017/")
# db = client["friends_birthdays"]
# collection = db["friends_collection"]

# # Remove the specified field from all documents
# update = {"$unset": {"month_day": ""}}

# # Update all documents in the collection
# collection.update_many({}, update)

# for doc in collection.find():
#     collection.update_one({'_id': doc['_id']}, {'$set': {'month_number': doc['birthday'].month}})
