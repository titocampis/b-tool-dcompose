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
collection = db["friends_collection"]

print(f"[{datetime.today()}]: Starting the daily birthday checking")

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
receiver_mail_username = "acalmazan98@gmail.com"
subject = "You have friends birthdays today"
# Body is incomplete, later we will add the birthdays day
body = (
    "Hello Alex, how are you doing today? "
    "You're the boss and you know it. But other than that, "
    "here are your friends who have birthdays today:\n\n"
)


# Get all friends from the collection
friends = f.get_friends(collection)

# Get today birthdays
lucky = ut.return_birthdays_today(friends)

# If there are no birthdays today
if not lucky:
    print("> No birthdays today")
else:
    # Output verbose
    print("> Today birthdays:")
    for key, value in lucky.items():

        message = (
            f" * {key}: {ut.calculate_old(value)} years "
            f"[{value.strftime('%B %d %Y')}]"
        )
        print(message)
        body += message + "\n"

    # Send the email
    print("\n> Sending the email")
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
