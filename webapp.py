import os

from flask import Flask, render_template

# from flask import jsonify, request
from pymongo import MongoClient

from mongodb import filters as mongodb_f
from utils import utilities as mut

# Get WS details from environment variables
WS_HOST = os.getenv("WS_HOST", "0.0.0.0")
WS_PORT = int(os.getenv("WS_PORT", "8080"))

# Get MongoDB connection details from environment variables
mongo_host = os.getenv("MONGO_HOST", "localhost")
mongo_port = int(os.getenv("MONGO_PORT", "27017"))

# Defining database
client = MongoClient(mongo_host, mongo_port)
db = client["friends_birthdays"]
friends_collection = db["friends_collection"]

# Defining the flask app name
app = Flask(__name__)


# Paths
@app.route("/")
def render_list():
    """Render the main page"""
    friends = mongodb_f.get_all_birthdays_sorted_by_month(friends_collection)
    return render_template(
        "base.html", friends=friends, calculate_old=mut.calculate_old
    )


# Paths
# @app.route('/<string:month>/')
# def render_index(month):
#     print(month)
#     return render_template('base.html', month=month)

print(WS_HOST + ":" + str(WS_PORT))

if __name__ == "__main__":
    app.run(host=WS_HOST, port=WS_PORT, debug=True)
