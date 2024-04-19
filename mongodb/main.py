from datetime import datetime
from pymongo import MongoClient, ASCENDING

import filters as f
import internal_queries as q

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["friends_birthdays"]
collection = db["friends_collection"]

name = "Ramon Garcia Cañabate"
birthday = datetime(1995, 11, 25, 0, 0)
sex = True
alias = "Ramonxu"
phone = "628658802"

friends = f.get_all_birthdays_sorted_by_month(collection)
print(friends['december'])
print("================")
print(f.get_birthdays_by_month(collection, 'december'))
