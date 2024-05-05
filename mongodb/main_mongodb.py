from datetime import datetime
from pymongo import MongoClient

from mongodb import filters as f, internal_queries as q
from mongodb import utilities as ut

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
    # q.update_by_name(collection, 'abel', 'birthday', datetime(1999, 8, 1))