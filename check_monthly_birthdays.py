import os
from datetime import datetime
from smtplib import SMTPException

from pymongo import MongoClient

from mongodb import filters as f
from utils import send_mail as sm
from utils import utilities as ut

# Get MongoDB connection details from environment variables
mongo_host = os.getenv("MONGO_HOST", "localhost")
mongo_port = int(os.getenv("MONGO_PORT", "27017"))

# Defining database
client = MongoClient(mongo_host, mongo_port)
db = client["friends_birthdays"]
friends_collection = db["friends_collection"]

today = datetime.today()
current_month = today.strftime("%B")

print(f"[{today}]: Starting the monthly [{current_month}] birthday checking")

# Retrieve secrets
try:
    sender_mail_username, sender_mail_password = ut.retrieve_secrets()
except FileNotFoundError as e:
    error_msg = f"[{datetime.now()}] [ERROR]: {e}"
    print(ut.st("red", error_msg))
    exit(1)
except PermissionError as pe:
    error_msg = f"[{datetime.now()}] [ERROR]: {pe}"
    print(ut.st("red", error_msg))
    exit(1)
except OSError as oe:
    error_msg = f"[{datetime.now()}] [ERROR]: {oe}"
    print(ut.st("red", error_msg))
    exit(1)
except Exception as e:  # pylint: disable=broad-exception-caught
    error_msg = f"[{datetime.now()}] [ERROR]: {e}"
    print(ut.st("red", error_msg))
    exit(1)

# Configure email
sender_name = "B-Tool Bot"
receiver_mail_username = "andreasscorelli@gmail.com"
subject = f"Friends Birthdays on {current_month}"
# Body is incomplete, later we will add the birthdays day
body = (
    f"Hello Alex, how are you doing this month, you have a lot of birthdays "
    f"did you know it? You have a lot of friends who have birthdays on "
    f"{current_month}, take a look on the list:\n\n"
)

# Get all friends who have birthdays on this month from friends_collection
friends = f.get_birthdays_by_month(friends_collection, current_month)

# If there are no birthdays today
if not friends:
    print(f"> No birthdays this month [{current_month}]")
else:
    # Output verbose
    print(f"> {current_month} Birthdays:")
    for friend in friends:

        message = (
            f" * {friend['birthday'].strftime('%B %d')} - {friend['name']} "
            f"({ut.calculate_old(friend['birthday'])})"
        )
        print(message)
        body += message + "\n"

    # Send the email
    print("> Sending the email")
    try:
        sm.send_mail(
            sender_mail_username,
            sender_mail_password,
            sender_name,
            receiver_mail_username,
            subject,
            body,
        )

    except ValueError as ve:
        error_msg = f"[{datetime.now()}] [ERROR]: {ve}"
        print(ut.st("red", error_msg))
        exit(1)

    except SMTPException as smtp_err:
        error_msg = f"[{datetime.now()}] [ERROR]: {smtp_err}"
        print(ut.st("red", error_msg))
        exit(1)

    except Exception as e:  # pylint: disable=broad-exception-caught
        error_msg = f"[{datetime.now()}] [ERROR]: {e}"
        print(ut.st("red", error_msg))
        exit(1)
