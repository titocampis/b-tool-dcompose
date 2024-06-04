from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import os

from mongodb import filters as mongodb_f
from utils import utilities as mut
from utils import send_mail as sm

# Variables
receiver_mail = 'marlot.vital@gmail.com'

## If docker compose
# WS_HOST = os.environ.get('WS_HOST')
# WS_PORT = os.environ.get('WS_PORT')

## If locally
WS_HOST = '0.0.0.0'
WS_PORT = 8080

# Retrieve secrets
sender_mail_username = mut.retrieve_secret(os.environ.get('SECRET_MAIL_USERNAME_FILE'))
sender_mail_password = mut.retrieve_secret(os.environ.get('SECRET_MAIL_PASSWORD_FILE'))

# MongoDB database info
client = MongoClient("mongodb://localhost:27017/")
db = client["friends_birthdays"]
collection = db["friends_collection"]

# Defining the flask app name
app = Flask(__name__)

# Paths
@app.route('/')
def render_list():
    '''Render the main page'''
    friends = mongodb_f.get_all_birthdays_sorted_by_month(collection)
    return render_template('base.html', friends=friends, calculate_old=mut.calculate_old)

# Paths
# @app.route('/<string:month>/')
# def render_index(month):
#     print(month)
#     return render_template('base.html', month=month)

if __name__ == "__main__":
    app.run(host=WS_HOST, port=WS_PORT, debug=True)
