from pymongo import MongoClient, ASCENDING

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
    return collection.insert_one({"name": name, "birthday": birthday})

def remove_friend_by_name(collection, name):
    '''Method to remove a friend by its name'''
    result = collection.delete_one({"name": "Mario Alcaide Almazán"})
    
    # Check if the document was deleted successfully
    if result.deleted_count == 1:
        print(f"Document [{name}] deleted successfully.")
    else:
        print(f"Document with the name [{name}] not found.")

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