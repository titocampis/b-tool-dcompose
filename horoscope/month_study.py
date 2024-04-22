from datetime import datetime
from pymongo import MongoClient

import matplotlib.pyplot as plt
from mongodb import filters as mongodb_f

# Defining database
client = MongoClient("mongodb://localhost:27017/")
db = client["friends_birthdays"]
collection = db["friends_collection"]

# Getting all your friends birthdays sorted by month
friends = mongodb_f.get_all_birthdays_sorted_by_month(collection)

months = friends.values()

friends = []

for month in months: 
    count = 0
    for friend in month:
        if friend['name'] != 'Dia Del Padre' and friend['name'] != 'Dia De La Madre' and 'Aniversario' not in friend['name']: count += 1
    friends.append(count)

plt.figure("Friends Affinity")
axis_x = range(1, len(months)+1)
plt.xticks(axis_x)
plt.xlabel('Month')
plt.ylabel('Nº Friends')
bars = plt.bar(axis_x, friends)

# Adding text annotations
for i, bar in enumerate(bars):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
             str(friends[i]), ha='center', va='bottom')

plt.show()
