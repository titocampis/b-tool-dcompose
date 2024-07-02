import os
import unicodedata as uni
from datetime import datetime


def st(style: str, msg: str) -> str:
    """
    Method to format a string based on style.

    Parameters:
    style (str): Style to choose.
    msg (str): String to format.

    Returns:
    str: msg formated.
    """

    styles = {
        # Colors Definition
        "HEADER": "\033[95m",
        "BLUE": "\033[94m",
        "CYAN": "\033[96m",
        "GREEN": "\033[92m",
        "OK": "\033[92m][OK]: ",
        "YEL": "\033[93m",
        "WARN": "\033[93m[WARNING]: ",
        "RED": "\033[91m",
        "ERROR": "\033[91m[ERROR]: ",
        "ENDC": "\033[0m",
        "BOLD": "\033[1m",
        "UNDERLINE": "\033[4m",
    }

    if style.upper() in styles.keys():
        return f"{styles[style.upper()]}{msg}{styles['ENDC']}"
    else:
        print(
            f"{styles['ERROR']}"
            f"No style available to transform the string {msg}"
        )
        exit(1)


def remove_accents_and_title(input_string: str) -> str:
    """
    Method to remove accents and use Title Format.

    Parameters:
    input_string (str): String to format.

    Returns:
    str: input_string formated.
    """
    # Remove accents
    normalized_string = (
        uni.normalize("NFD", input_string)
        .encode("ascii", "ignore")
        .decode("utf-8")
    )

    # Capitalize first word (title case)
    title_case_string = normalized_string.title()

    return title_case_string


def check_birthday(birthday: datetime) -> list:
    """
    Method to check birthday content is datetime object and if it is,
    return birthday, month, month_number, birthday.day

    Parameters:
    birtdhay (datetime): Datetime to check and retrieve month, day, etc.

    Returns:
    list([birthday, month, month_number, birthday.day]) if birthday is datetime
    """
    if isinstance(birthday, datetime):

        # Extract the month component
        month_number = birthday.month
        month = birthday.strftime("%B").lower()

        return birthday, month, month_number, birthday.day
    else:
        error_msg = (
            f"Invalid birthday value [{birthday}]. "
            f"Birthday field must be a datetime object."
        )
        print(st("error", error_msg))
        exit(1)


def check_sex(sex: bool) -> bool:
    """
    Method to check sex content is boolean

    Parameters:
    sex (bool): True if boy, False if girl.

    Returns:
    sex (bool): Same value just if it is boolean.
    """
    if isinstance(sex, bool):
        return sex
    else:
        error_msg = f"Invalid sex value [{sex}]. Sex field must be boolean."
        print(st("error", error_msg))
        exit(1)


def check_phone(phone: str) -> str:
    """
    Method to check phone content is double with 9 positions

    Parameters:
    phone (str): A phone number.

    Returns:
    phone (str): The phone number if it is double with 9 positions.
    """
    # Remove any non-digit characters from the phone number
    cleaned_number = "".join(filter(str.isdigit, phone))

    # Check if the cleaned number has exactly 9 digits
    if len(cleaned_number) == 9:
        return phone
    else:
        error_msg = (
            f"Invalid phone value [{phone}]. "
            f"Phone field must be a number of 9 digits."
        )
        print(st("error", error_msg))
        exit(1)


def calculate_old(birthday: datetime) -> int:
    """
    Method to calculate how many years a person
    is going to have on his birthday

    Parameters:
    birthday (datetime): A birthday.

    Returns:
    age (int): The age a person whith this birthday is going to have this year.
    """
    # Check if the birthday is datetime
    if isinstance(birthday, datetime):

        # Calculate the age
        today = datetime.now()
        age = today.year - birthday.year

        # Make the adjustmen depending on day and month
        # (not used because its not his birthday today)
        # if (
        #   today.month < birthday.month
        #   or (today.month == birthday.month and today.day < birthday.day)
        # ):
        #     age -= 1

        return age
    else:
        error_msg = (
            f"Invalid birthday value [{birthday}]. "
            f"Birthday field must be a datetime object."
        )
        print(st("error", error_msg))
        exit(1)


def read_secret(secret_path: str) -> str:
    """
    Method which reads the contents of a file and returns its contents
    as a string, with leading and trailing whitespace removed

    Parameters:
    secret_path (str): The path to the secret file.

    Returns:
    str: The contents of the file with leading and trailing whitespace removed.

    Raises:
    FileNotFoundError: If the file does not exist.
    PermissionError: If there is an issue with file permissions.
    OSError: If there is an I/O error.
    """
    try:
        with open(secret_path, encoding="utf-8") as secret_file:
            return secret_file.read().strip()

    except FileNotFoundError as fe:
        raise FileNotFoundError(
            f"The file at {secret_path} was not found. {fe}"
        ) from fe
    except PermissionError as pe:
        raise PermissionError(
            f"Permission denied when accessing the file at {secret_path}. {pe}"
        ) from pe
    except OSError as oe:
        raise OSError(
            f"An I/O error occurred when accessing the file "
            f"at {secret_path}: {oe}"
        ) from oe


def retrieve_secrets() -> tuple[str, str]:
    """
    Method specific for this app to retrieve the needed secrets
    from the configured files

    Returns:
    Tuple[str, str]: A tuple containing the sender mail username and password.

    Raises:
    KeyError: If any required environment variable is not set.
    FileNotFoundError: If any of the secret files are not found.
    OSError: If there is an I/O error when reading the files.
    Exception: For any other exceptions that occur.
    """
    try:
        username_file = os.environ.get("SECRET_MAIL_USERNAME_FILE")
        password_file = os.environ.get("SECRET_MAIL_PASSWORD_FILE")

        if username_file is None:
            raise OSError(
                "Environment variable SECRET_MAIL_USERNAME_FILE is not set."
            )
        if password_file is None:
            raise OSError(
                "Environment variable SECRET_MAIL_PASSWORD_FILE is not set."
            )

        sender_mail_username = read_secret(username_file)
        sender_mail_password = read_secret(password_file)

        return sender_mail_username, sender_mail_password

    except FileNotFoundError as e:
        raise FileNotFoundError(f"Secret file not found: {e.filename}") from e
    except PermissionError as pe:
        raise PermissionError(pe) from pe
    except OSError as oe:
        raise OSError(oe) from oe


def return_birthdays_today(friends: dict) -> dict:
    """
    Method which returns all today friends birthdays from a friends dict
    and return them into another dict

    Parameters:
    friends (dict): a dictionary with all the friedns to check.

    Returns:
    dict: a dictionary with all friends which birthday is today.
    """

    # Retrieving today from datetime
    today = datetime.now()

    # Dictionary with friends which birthday is today
    lucky = {}

    # Check for each friend if its birthday is today
    for friend in friends:
        if (
            friend["birthday"].day == today.day
            and friend["birthday"].month == today.month
        ):
            lucky[friend["name"]] = friend["birthday"]

    # Return the dictionary
    return lucky
