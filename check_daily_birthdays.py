from datetime import datetime
import os
from pymongo import MongoClient

from mongodb import filters as f
from utils import utilities as ut, send_mail as sm

# MongoDB database info
client = MongoClient("mongodb://localhost:27017/")
db = client["friends_birthdays"]
collection = db["friends_collection"]

print(f"[{datetime.today()}]: Starting the daily birthday checking")

# Uncomment for local Executions
# sender_mail_username = ''
# sender_mail_password = ''

# Retrieve secrets
# sender_mail_username = ut.retrieve_secret(os.environ.get('SECRET_MAIL_USERNAME_FILE'))
# sender_mail_password = ut.retrieve_secret(os.environ.get('SECRET_MAIL_PASSWORD_FILE'))

# Configure email
sender_name = 'B-Tool Bot'
receiver_mail_username = 'andreasscorelli@gmail.com'
subject = 'You have friends birthdays today'
# Body is incomplete, later we will add the birthdays day
body = f"""
Hello Alex, how are you doing today?
You're the boss and you know it. But other than that, here are your friends who have birthdays today:\n
"""
        
# Get all friends from the collection
friends = f.get_friends(collection)

# Get today birthdays
lucky = ut.return_birthdays_today(collection, friends)

# If there are no birthdays today
if not lucky: print('> No birthdays today')
else: 
    # Output verbose
    print('> Today birthdays:')
    for key, value in lucky.items(): 
        print(f" * {key}: {ut.calculate_old(value)} years [{value.strftime('%B %d %Y')}]")
        body += f" * {key}: {ut.calculate_old(value)} years [{value.strftime('%B %d %Y')}]\n"
    
    # Send the email
    print('\n> Sending the email')
    sm.send_mail(sender_mail_username, sender_mail_password, sender_name, receiver_mail_username, subject, body)
