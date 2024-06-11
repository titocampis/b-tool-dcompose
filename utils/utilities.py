from datetime import datetime
import os
import unicodedata as uni

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def remove_accents_and_title(input_string:str):
    # Remove accents
    normalized_string = uni.normalize('NFD', input_string).encode('ascii', 'ignore').decode('utf-8')
    
    # Capitalize first word (title case)
    title_case_string = normalized_string.title()
    
    return title_case_string

def check_birthday(birthday:datetime):
    '''Method to check birthday content is datetime object'''
    if isinstance(birthday, datetime): 
        
        # Extract the month component
        month_number = birthday.month
        month = birthday.strftime("%B").lower()
        
        return birthday, month, month_number, birthday.day
    else:
        print(f"{bcolors.FAIL}Invalid birthday value [{birthday}]. Birthday field must be a datetime object.{bcolors.ENDC}")
        exit(1)

def check_sex(sex:bool):
    '''Method to check sex content is boolean'''
    if isinstance(sex, bool): return sex
    else:
        print(f"{bcolors.FAIL}Invalid sex value [{sex}]. Sex field must be boolean.{bcolors.ENDC}")
        exit(1)

def check_phone(phone:str):
    '''Method to check phone content is double and for 9 numbers'''
    # Remove any non-digit characters from the phone number
    cleaned_number = ''.join(filter(str.isdigit, phone))

    # Check if the cleaned number has exactly 9 digits
    if len(cleaned_number) == 9:
        return phone
    else:
        print(f"{bcolors.FAIL}Invalid phone value [{phone}]. Phone field must be a number of 9 digits.{bcolors.ENDC}")
        exit(1)

def calculate_old(birthday:datetime):
    '''Method to calculate how many years a person is going to have on his birthday'''

    # Check if the birthday is datetime
    if isinstance(birthday, datetime):
        
        # Calculate the age
        today = datetime.now()
        age = today.year - birthday.year

        # Make the adjustmen depending on day and month - Not used because its not his birthday today
        # if today.month < birthday.month or (today.month == birthday.month and today.day < birthday.day):
        #     age -= 1

        return age
    else:
        print(f"{bcolors.FAIL}Invalid birthday value [{birthday}]. Birthday field must be a datetime object.{bcolors.ENDC}")
        exit(1)

def read_secret(secret_path:str):
    '''Method which reads the contents of a file and returns its contents as a string, with leading and trailing whitespace removed'''
    with open(secret_path, 'r') as secret_file:
        return secret_file.read().strip()
    
def retrieve_secrets():
    '''Method specific for this app to retrieve the needed secrets from the configured files'''
    try:
        sender_mail_username = read_secret(os.environ.get('SECRET_MAIL_USERNAME_FILE'))
        sender_mail_password = read_secret(os.environ.get('SECRET_MAIL_PASSWORD_FILE'))
        return sender_mail_username, sender_mail_password

    except FileNotFoundError as e:
        print(f"Error: Secret file not found: {e.filename}")

    except Exception as e:
        print(f"Error: An error ocurred parsing the secrets files: {e}")


def return_birthdays_today(birthday:datetime, friends:dict):
    '''Method which returns all today friends birthdays of some friend checking the db and returning a dict with this data and its birthday'''
    
    # Retrieving today from datetime
    today = datetime.now()

    # Dictionary with friends which birthday is today
    lucky = {}

    # Check for each friend if its birthday is today
    for friend in friends:
        if friend['birthday'].day == today.day and friend['birthday'].month == today.month: lucky[friend['name']] = friend['birthday']

    # Return the dictionary
    return lucky
