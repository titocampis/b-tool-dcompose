from datetime import datetime
from pymongo import MongoClient

import json
import matplotlib.pyplot as plt
from mongodb import filters as mongodb_f

################################ MAIN OF MONGODB ################################ 
# This main is an example of how to use mongodb module 
################################################################################# 

# Defining database
client = MongoClient("mongodb://localhost:27017/")
db = client["friends_birthdays"]
collection = db["friends_collection"]

# Defining horoscopes
horoscopes = {
    "aquarius": {
        "start": datetime(1900,1,20),
        "end": datetime(1900,2,18)
    },
    "pisces": {
        "start": datetime(1900,2,19),
        "end": datetime(1900,3,20)
    },
    "aries": {
        "start": datetime(1900,3,21),
        "end": datetime(1900,4,19)
    },
    "taurus": {
        "start": datetime(1900,4,20),
        "end": datetime(1900,5,20)
    },
    "gemini": {
        "start": datetime(1900,5,21),
        "end": datetime(1900,6,20)
    },
    "cancer": {
        "start": datetime(1900,6,21),
        "end": datetime(1900,7,22)
    },
    "leo": {
        "start": datetime(1900,7,23),
        "end": datetime(1900,8,22)
    },
    "virgo": {
        "start": datetime(1900,8,23),
        "end": datetime(1900,9,22)
    },
    "libra": {
        "start": datetime(1900,9,22),
        "end": datetime(1900,10,22)
    },
    "scorpio": {
        "start": datetime(1900,10,23),
        "end": datetime(1900,11,21)
    },
    "sagittarius": {
        "start": datetime(1900,11,22),
        "end": datetime(1900,12,21)
    },
    "capricorn": {
        "start": datetime(1900,12,22),
        "end": datetime(1900,1,19)
    }
}

# Getting all your friends birthdays sorted by month
friends = mongodb_f.get_friends(collection)

# Function to calculate the horoscope based on the birthday
def calculate_horoscope(birthday_homogenized, horoscopes):
    for horoscope, horoscope_dates in horoscopes.items():
        if horoscope == 'capricorn':
            if horoscope_dates['start'] <= birthday_homogenized or birthday_homogenized <= horoscope_dates['end']: return horoscope
        else:
            if horoscope_dates['start'] <= birthday_homogenized <= horoscope_dates['end']: return horoscope
    return None

friends_horoscopes = []
for friend in friends:
    if friend['name'] != 'Dia Del Padre' and friend['name'] != 'Dia De La Madre' and 'Aniversario' not in friend['name']:
        birthday_homogenized = datetime(1900, friend['birthday'].month, friend['birthday'].day)
        friends_horoscopes.append(calculate_horoscope(birthday_homogenized, horoscopes))

horoscopes_count = [friends_horoscopes.count('aquarius'),
                   friends_horoscopes.count('pisces'),
                   friends_horoscopes.count('aries'),
                   friends_horoscopes.count('taurus'),
                   friends_horoscopes.count('gemini'),
                   friends_horoscopes.count('cancer'),
                   friends_horoscopes.count('leo'),
                   friends_horoscopes.count('virgo'),
                   friends_horoscopes.count('libra'),
                   friends_horoscopes.count('scorpio'),
                   friends_horoscopes.count('sagittarius'),
                   friends_horoscopes.count('capricorn'),
                   ]

print(horoscopes_count)
print(list(horoscopes.keys()))

plt.figure("Horoscopes Affinity")
axis_x = range(1, len(horoscopes_count)+1)
plt.xticks(axis_x, list(horoscopes.keys()))
plt.xlabel('Horoscope')
plt.ylabel('Nº Friends')
bars = plt.bar(axis_x, horoscopes_count)

# Adding text annotations
for i, bar in enumerate(bars):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
             str(horoscopes_count[i]), ha='center', va='bottom')

plt.show()
