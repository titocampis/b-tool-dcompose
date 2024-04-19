from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient, ASCENDING

import mongodb.filters as mongodb_f

# Defining the flask app name
app = Flask(__name__)

# Variables
WS_HOST = "0.0.0.0"
WS_PORT = 8080

# MongoDB database info
client = MongoClient("mongodb://localhost:27017/")
db = client["friends_birthdays"]
collection = db["friends_collection"]

# Auxiliar functions

# Paths
# @app.route('/<string:month>/')
# def render_index(month):
#     print(month)
#     return render_template('base.html', month=month)

@app.route('/list/')
def render_list():
    '''Render the main page'''
    friends = mongodb_f.get_all_birthdays_sorted_by_month(collection)
    return render_template('base.html', friends=friends)

if __name__ == "__main__":
    app.run(host=WS_HOST, port=WS_PORT, debug=True)
