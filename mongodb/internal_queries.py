from datetime import datetime
from pymongo import MongoClient, ASCENDING
from pymongo.errors import OperationFailure
import unicodedata as uni

import utilities as ut

def create_birthday_index(collection):
    '''Method to create the birthday index to notify it is a datetime (not enforce)'''
    # Define the index specification
    index_spec = [("birthday", ASCENDING)]

    # Create the index with the partial filter expression
    try:
        collection.create_index(index_spec, partialFilterExpression={"birthday": {"$type": "date"}})
        print(f"Index for [{ut.bcolors.OKCYAN}birthday{ut.bcolors.ENDC}] created successfully")
    except OperationFailure as e:
        print(f"{ut.bcolors.FAIL}Error creating index: {e}{ut.bcolors.ENDC}")


def get_indexes(collection):
    '''Method to return all the indexes in the collection'''
    indexes = collection.list_indexes()
    for index in indexes:
        print(index['name'],'-->', index)


def insert_friend(collection, name, birthday, sex, alias, phone):
    '''Method to insert friend data into the collection'''
    
    birthday, month, month_number, day = ut.check_birthday(birthday)
    user = {"name": ut.remove_accents_and_title(name), 
            "birthday": birthday,
            "month": month,
            "month_number": month_number,
            "day": day, 
            "sex": ut.check_sex(sex),
            "alias": ut.remove_accents_and_title(alias), 
            "phone": ut.check_phone(phone)}
    
    result = collection.insert_one(user)
    # Check if the user has been added
    if result.acknowledged: print(f"User [name={ut.bcolors.OKCYAN}{name}{ut.bcolors.ENDC}] has been correctly added to the collection.\n{user}")
    else: print(f"{ut.bcolors.FAIL}User [name={name}] has not been added to the collection.{ut.bcolors.ENDC}")


def remove_friend_by_name(collection, name):
    '''Method to remove a friend by its name'''
    name = ut.remove_accents_and_title(name)
    result = collection.delete_one({"name": name})
    
    # Check if the document was deleted successfully
    if result.deleted_count == 1:
        print(f"Document with [{ut.bcolors.OKCYAN}name={name}{ut.bcolors.ENDC}] deleted successfully.")
    else:
        print(f"{ut.bcolors.FAIL}Document with [name={name}] not found.{ut.bcolors.ENDC}")


def get_friends(collection):
    '''Method to check the entries in the collection'''
    # Find all documents in the collection
    cursor = collection.find({}).sort([("month_number", ASCENDING), ("day", ASCENDING)])

    # Iterate over the cursor to print each document
    for document in cursor:
        print(document)


def update_by_name(collection, name, field, content):
    '''Method to update a field of a friend by its name'''
    # Check the field wanted to update
    field = field.lower()
    if field == 'name': content = ut.remove_accents_and_title(content)
    elif field == 'birthday': ut.check_birthday(content)
    elif field == 'phone': ut.check_phone(content)
    elif field == 'sex': ut.check_sex(content)
    elif field == 'alias': content = ut.remove_accents_and_title(content)
    else:
        print(f"{ut.bcolors.FAIL}Update failed, invalid field [{field}], choose one valid [birthday, phone, sex, alias]")
        exit(1)
    
    # Homogenize the name
    name = ut.remove_accents_and_title(name)

    # Specify the filter (query) to find the document(s) to update
    filter_query = {"name": name}

    # Specify the update operation
    update_operation = {"$set": {field: content}}

    # Update one document that matches the filter
    update_result = collection.update_one(filter_query, update_operation)
    # Check if the update was successful
    if not update_result.acknowledged: print(f"{ut.bcolors.FAIL}Something went wrong stablishing the connection{ut.bcolors.ENDC}]\n{update_result}")
    elif update_result.matched_count == 0: print(f"{ut.bcolors.FAIL}Update failed, no documents matched the filter criteria: [name={name}]\n{update_result}{ut.bcolors.ENDC}")
    elif update_result.modified_count == 1: print(f"Document [{ut.bcolors.OKCYAN}name={name}{ut.bcolors.ENDC}] updated successfully: [{ut.bcolors.OKCYAN}{field}={content}{ut.bcolors.ENDC}]")
    elif update_result.modified_count == 0: print(f"{ut.bcolors.WARNING}Nothing to modify, the document with [name={name}] already match the field [{field}={content}]{ut.bcolors.ENDC}")
    else: print(f"{ut.bcolors.FAIL}Something went wrong: {update_result}{ut.bcolors.ENDC}")
    
    
    # With birthday we update 2 fields, birthday and month
    if field == 'birthday':
        update_operation2 = {"$set": {'month': ut.check_birthday(content)[1]}}
        
        # Update one document that matches the filter
        update_result = collection.update_one(filter_query, update_operation2)
        # Check if the update was successful
        if not update_result.acknowledged: print(f"{ut.bcolors.FAIL}Something went wrong stablishing the connection{ut.bcolors.ENDC}]\n{update_result}")
        elif update_result.matched_count == 0: print(f"{ut.bcolors.FAIL}Update failed, no documents matched the filter criteria: [name={name}]\n{update_result}{ut.bcolors.ENDC}")
        elif update_result.modified_count == 1: print(f"Document [{ut.bcolors.OKCYAN}name={name}{ut.bcolors.ENDC}] updated successfully: [{ut.bcolors.OKCYAN}month={ut.check_birthday(content)[1]}{ut.bcolors.ENDC}]")
        elif update_result.modified_count == 0: print(f"{ut.bcolors.WARNING}Nothing to modify, the document with [name={name}] already match the field [month={ut.check_birthday(content)[1]}]{ut.bcolors.ENDC}")
        else: print(f"{ut.bcolors.FAIL}Something went wrong: {update_result}{ut.bcolors.ENDC}")
