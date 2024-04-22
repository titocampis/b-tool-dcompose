from datetime import datetime

def date2datetime(date):
    '''Method to transform date into datetime'''
    month, day = date.split("-")
    return datetime(1000, int(month), int(day))

def homogenize_birthday(date):
    '''Method to transform a full datetime into a datetime with year 1000 and month and day'''
    return datetime(1000, date.month, date.day)

def calculate_horoscope(birthday_homogenized, horoscopes):
    '''Method to calculate the horoscope based on the birthday'''
    for horoscope, horoscope_dates in horoscopes.items():
        if horoscope == 'capricorn':
            if horoscope_dates['start'] <= birthday_homogenized or birthday_homogenized <= horoscope_dates['end']: return horoscope
        else:
            if horoscope_dates['start'] <= birthday_homogenized <= horoscope_dates['end']: return horoscope
    return None
