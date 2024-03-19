for doc in collection.find():
    # Extract the month from the birthday field
    month = doc['birthday'].month
    
    if month == 1:
        month = 'january'
    elif month == 2:
        month = 'february'
    elif month == 3:
        month = 'march'
    elif month == 4:
        month = 'april'
    elif month == 5:
        month = 'may'
    elif month == 6:
        month = 'june'
    elif month == 7:
        month = 'july'
    elif month == 8:
        month = 'august'
    elif month == 9:
        month = 'september'
    elif month == 10:
        month = 'october'
    elif month == 11:
        month = 'november'
    else:
        month = 'december'
    
    # Update the document in the collection
    collection.update_one({'_id': doc['_id']}, {'$set': {'month': month}})
