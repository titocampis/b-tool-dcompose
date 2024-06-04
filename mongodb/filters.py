from pymongo import ASCENDING

import utils.utilities as ut

def get_friends(collection):
    '''Method which returns all the entries in the collection as list'''
    return list(collection.find({}).sort([("month_number", ASCENDING), ("day", ASCENDING)]))

def get_friend_by_name(collection, name):
    '''Method which returns a document searching by its name'''
    return collection.find_one({"name": ut.remove_accents_and_title(name)})

def get_friend_by_alias(collection, alias):
    '''Method which returns a document searching by its alias (it can be more than one)'''
    return list(collection.find({"alias": ut.remove_accents_and_title(alias)}))
        
def get_birthdays_by_month(collection, target_month):
    '''Method which returns the birthdays of a month as list'''
    return list(collection.find({"month": target_month.lower()}).sort("day", ASCENDING))

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
