from datetime import datetime
from pymongo import MongoClient, ASCENDING
from pymongo.errors import OperationFailure
import unicodedata as uni

import utilities as ut

def get_friend_by_name(collection, name):
    '''Method which returns a document searching by its name'''
    result = collection.find_one({"name": ut.remove_accents_and_title(name)})
    print(result)


def get_friend_by_alias(collection, alias):
    '''Method which returns a document searching by its alias'''
    results = collection.find({"alias": ut.remove_accents_and_title(alias)})
    # As it can be a string (more than one)
    for result in results:
        print(result)
        
def get_birthdays_by_month(collection, target_month):
    '''Method which returns the birthdays of a month'''
    print(ut.remove_accents_and_title(target_month))
    results = collection.find({"month": target_month.lower()})
    # As it can be a string (more than one)
    for result in results:
        print(result)