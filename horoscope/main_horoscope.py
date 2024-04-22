from pymongo import MongoClient

import json
import matplotlib.pyplot as plt
from mongodb import filters as mongodb_f
from horoscope import horoscope_study as hs

def main_horoscope():
    # Defining database
    client = MongoClient("mongodb://localhost:27017/")
    db = client["friends_birthdays"]
    collection = db["friends_collection"]

    # Loading the json
    with open('horoscope/horoscopes.json', 'r') as file:
        horoscopes_dict = json.load(file)

    # Converting simple dates on datetimes
    for horoscope in horoscopes_dict.values():
        horoscope['start'] = hs.date2datetime(horoscope['start'])
        horoscope['end'] = hs.date2datetime(horoscope['end'])

    # Getting all your friends birthdays sorted by month
    friends = mongodb_f.get_friends(collection)


    friends_horoscopes = []
    for friend in friends:
        if friend['name'] != 'Dia Del Padre' and friend['name'] != 'Dia De La Madre' and 'Aniversario' not in friend['name']:
            birthday_homogenized = hs.homogenize_birthday(friend['birthday'])
            friends_horoscopes.append(hs.calculate_horoscope(birthday_homogenized, horoscopes_dict))

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
    print(list(horoscopes_dict.keys()))

    plt.figure("Horoscopes Affinity")
    axis_x = range(1, len(horoscopes_count)+1)
    plt.xticks(axis_x, list(horoscopes_dict.keys()))
    plt.xlabel('Horoscope')
    plt.ylabel('Nº Friends')
    bars = plt.bar(axis_x, horoscopes_count)

    # Adding text annotations
    for i, bar in enumerate(bars):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
                str(horoscopes_count[i]), ha='center', va='bottom')

    plt.show()
