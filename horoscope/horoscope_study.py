from datetime import datetime

def date2datetime(date):
    '''Method to transform date into datetime'''
    month, day = date.split("-")
    return datetime(1000, int(month), int(day))
