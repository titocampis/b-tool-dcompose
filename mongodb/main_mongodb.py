from datetime import datetime
from pymongo import MongoClient

import mongodb.filters as f
import mongodb.internal_queries as q

################################ MAIN OF MONGODB ################################ 
# This main is an example of how to use mongodb module 
################################################################################# 

def main_mongodb():
    # Defining database
    client = MongoClient("mongodb://localhost:27017/")
    db = client["friends_birthdays"]
    collection = db["friends_collection"]

    name = "Ramon Garcia Cañabate"
    birthday = datetime(1995, 11, 25, 0, 0)
    sex = True
    alias = "Ramonxu"
    phone = "628658802"

    friends = f.get_all_birthdays_sorted_by_month(collection)
    print(friends['january'], "\n=========================================")
    for elem in friends.keys():
        print(friends[elem])
