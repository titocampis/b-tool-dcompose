from datetime import datetime
from pymongo import MongoClient

from mongodb import filters as f
from utils import utilities as ut, send_mail as sm

# MongoDB database info
client = MongoClient("mongodb://localhost:27017/")
db = client["friends_birthdays"]
collection = db["friends_collection"]

today = datetime.today()
current_month = today.strftime("%B")

print(f"[{today}]: Starting the monthly [{current_month}] birthday checking")

# Retrieve secrets
sender_mail_username, sender_mail_password = ut.retrieve_secrets()

# Configure email
sender_name = 'B-Tool Bot'
receiver_mail_username = 'andreasscorelli@gmail.com'
subject = f"Friends Birthdays on {current_month}"
# Body is incomplete, later we will add the birthdays day
body = f"""
Hello Alex, how are you doing this month, you have a lot of birthdays, did you know it?
You have a lot of friends who have birthdays on {current_month}, take a look on the list:\n
"""
        
# Get all friends who have birthdays on this month
friends = f.get_birthdays_by_month(collection, current_month)

# If there are no birthdays today
if not friends: 
    print(f"> No birthdays this month [{current_month}]")
    # sm.send_mail(sender_mail_username, sender_mail_password, sender_name, receiver_mail_username, subject, f"You dont have friend birthdays this month [{current_month}] XD")
else: 
    # Output verbose
    print(f"> {current_month} Birthdays:")
    for friend in friends:
        print(f" * {friend['birthday'].strftime('%B %d')} - {friend['name']} ({ut.calculate_old(friend['birthday'])})")
        body += f" * {friend['birthday'].strftime('%B %d')} - {friend['name']} ({ut.calculate_old(friend['birthday'])})\n"
    
    # Send the email
    print('\n> Sending the email')
    sm.send_mail(sender_mail_username, sender_mail_password, sender_name, receiver_mail_username, subject, body)
