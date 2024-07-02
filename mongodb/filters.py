from pymongo import ASCENDING, collection

import utils.utilities as ut


def get_friends(friends_collection: collection) -> list:
    """
    Method which returns all the entries in the collection as list

    Parameters:
    collection (collection): database collection with all your friends.

    Returns:
    list: a list with all friends (dict) in friends_collection.
    """
    return list(
        friends_collection.find({}).sort(
            [("month_number", ASCENDING), ("day", ASCENDING)]
        )
    )


def get_friend_by_name(friends_collection: collection, name: str) -> dict:
    """
    Method which returns a document searching by its name

    Parameters:
    collection (collection): database collection with all your friends.
    name (str): name of the friend you want to retrieve.

    Returns:
    dict: friend data in dict.
    """
    return friends_collection.find_one(
        {"name": ut.remove_accents_and_title(name)}
    )


def get_friend_by_alias(friends_collection: collection, alias: str) -> list:
    """
    Method which retrieves a document by its alias (can be more than one)

    Parameters:
    collection (collection): database collection with all your friends.
    alias (str): alias of the friend you want to retrieve.

    Returns:
    list: a list with all friends (dict) with alias.
    """
    return list(
        friends_collection.find({"alias": ut.remove_accents_and_title(alias)})
    )


def get_birthdays_by_month(
    friends_collection: collection, target_month: str
) -> list:
    """
    Method which returns the birthdays of a month as list

    Parameters:
    collection (collection): database collection with all your friends.
    target_month (str): month of the year to search for birthdays.

    Returns:
    list: a list with all friends (dict) with birthday in target_month.
    """
    return list(
        friends_collection.find({"month": target_month.lower()}).sort(
            "day", ASCENDING
        )
    )


def get_all_birthdays_sorted_by_month(friends_collection: collection) -> dict:
    """
    Method which returns all the birthdays sorted by month in python dict

    Parameters:
    collection (collection): database collection with all your friends.

    Returns:
    dict: a dict with all friends birthdays sorted by month and day.
    """
    friends = {}
    friends["january"] = get_birthdays_by_month(friends_collection, "january")
    friends["february"] = get_birthdays_by_month(friends_collection, "february")
    friends["march"] = get_birthdays_by_month(friends_collection, "march")
    friends["april"] = get_birthdays_by_month(friends_collection, "april")
    friends["may"] = get_birthdays_by_month(friends_collection, "may")
    friends["june"] = get_birthdays_by_month(friends_collection, "june")
    friends["july"] = get_birthdays_by_month(friends_collection, "july")
    friends["august"] = get_birthdays_by_month(friends_collection, "august")
    friends["september"] = get_birthdays_by_month(
        friends_collection, "september"
    )
    friends["october"] = get_birthdays_by_month(friends_collection, "october")
    friends["november"] = get_birthdays_by_month(friends_collection, "november")
    friends["december"] = get_birthdays_by_month(friends_collection, "december")
    return friends
