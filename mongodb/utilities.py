from datetime import datetime
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

def remove_accents_and_title(input_string):
    # Remove accents
    normalized_string = uni.normalize('NFD', input_string).encode('ascii', 'ignore').decode('utf-8')
    
    # Capitalize first word (title case)
    title_case_string = normalized_string.title()
    
    return title_case_string

def check_birthday(birthday):
    '''Method to check birthday content is datetime object'''
    if isinstance(birthday, datetime): 
        
        # Extract the month component
        month_number = birthday.month
        if month_number == 1: month = 'january'
        elif month_number == 2: month = 'february'
        elif month_number == 3: month = 'march'
        elif month_number == 4: month = 'april'
        elif month_number == 5: month = 'may'
        elif month_number == 6: month = 'june'
        elif month_number == 7: month = 'july'
        elif month_number == 8: month = 'august'
        elif month_number == 9: month = 'september'
        elif month_number == 10: month = 'october'
        elif month_number == 11: month = 'november'
        else: month = 'december'
        
        return birthday, month, month_number, birthday.day
    else:
        print(f"{bcolors.FAIL}Invalid birthday value [{birthday}]. Birthday field must be a datetime object.{bcolors.ENDC}")
        exit(1)

def check_sex(sex):
    '''Method to check sex content is boolean'''
    if isinstance(sex, bool): return sex
    else:
        print(f"{bcolors.FAIL}Invalid sex value [{sex}]. Sex field must be boolean.{bcolors.ENDC}")
        exit(1)

def check_phone(phone):
    '''Method to check phone content is double and for 9 numbers'''
    # Remove any non-digit characters from the phone number
    cleaned_number = ''.join(filter(str.isdigit, phone))

    # Check if the cleaned number has exactly 9 digits
    if len(cleaned_number) == 9:
        return phone
    else:
        print(f"{bcolors.FAIL}Invalid phone value [{phone}]. Phone field must be a number of 9 digits.{bcolors.ENDC}")
        exit(1)

def calculate_old(birthday):
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
