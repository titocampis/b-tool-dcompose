from datetime import datetime
from pymongo import MongoClient, ASCENDING
from pymongo.errors import OperationFailure
import unicodedata as uni

import mongodb.utilities as ut

def get_friend_by_name(collection, name):
    '''Method which returns a document searching by its name'''
    result = collection.find_one({"name": ut.remove_accents_and_title(name)})
    return list(result)


def get_friend_by_alias(collection, alias):
    '''Method which returns a document searching by its alias'''
    results = collection.find({"alias": ut.remove_accents_and_title(alias)})
    # As it can be more than one
    return list(results)
        
def get_birthdays_by_month(collection, target_month):
    '''Method which returns the birthdays of a month'''
    # print(ut.remove_accents_and_title(target_month))
    results = collection.find({"month": target_month.lower()}).sort("day", ASCENDING)
    return list(results)

def get_all_birthdays_sorted_by_month(collection):
    '''Method which returns all the birthdays sorted by month in a python dict'''
    friends = {}
    friends['january'] = get_birthdays_by_month(collection, 'january') 
    friends['february'] = get_birthdays_by_month(collection, 'february')
    friends['march'] = get_birthdays_by_month(collection, 'march')
    friends['april'] = get_birthdays_by_month(collection, 'april')
    friends['may'] = get_birthdays_by_month(collection, 'may')
    friends['june'] = get_birthdays_by_month(collection, 'june')
    friends['july'] = get_birthdays_by_month(collection, 'july')
    friends['august'] = get_birthdays_by_month(collection, 'august')
    friends['september'] = get_birthdays_by_month(collection, 'september')
    friends['october'] = get_birthdays_by_month(collection, 'october')
    friends['november'] = get_birthdays_by_month(collection, 'november')
    friends['december'] = get_birthdays_by_month(collection, 'december')
    return friends
