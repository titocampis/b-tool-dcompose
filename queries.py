from pymongo import MongoClient, ASCENDING
import unicodedata as uni

import utilities as ut

def create_unique_index(collection, field):
    '''Method to create an index to unique field'''
    return collection.create_index([(field, ASCENDING)], unique=True)

def check_indexes(collection):
    '''Method to return all the indexes in the collection'''
    indexes = collection.list_indexes()
    
    # Print each index
    for index in indexes:
        print(index)

def insert_friend(collection, name, birthday):
    '''Method to insert friend data into the collection'''
    name = ut.remove_accents_and_title(name)
    result = collection.insert_one({"name": name, "birthday": birthday})
    
    # Check if the user has been added
    if result.acknowledged: print(f"User [name={ut.bcolors.OKCYAN}{name}{ut.bcolors.ENDC}] has been correctly added to the collection.")
    else: print(f"{ut.bcolors.FAIL}User [name={name}] has not been added to the collection.{ut.bcolors.ENDC}")

def remove_friend_by_name(collection, name):
    '''Method to remove a friend by its name'''
    name = ut.remove_accents_and_title(name)
    result = collection.delete_one({"name": name})
    
    # Check if the document was deleted successfully
    if result.deleted_count == 1:
        print(f"Document with [name={ut.bcolors.OKCYAN}{name}{ut.bcolors.ENDC}] deleted successfully.")
    else:
        print(f"{ut.bcolors.FAIL}Document with [name={name}] not found.{ut.bcolors.ENDC}")

def check_friends(collection):
    '''Method to check the entries in the collection'''
    # Find all documents in the collection
    cursor = collection.find({})

    # Iterate over the cursor to print each document
    for document in cursor:
        print(document)

def check_friend_by_name(collection, name):
    '''Method which returns a document searching by its name'''
    result = collection.find_one({"name": name})
    print(result)