from datetime import datetime

from pymongo import ASCENDING, collection
from pymongo.errors import OperationFailure

import utils.utilities as ut


def create_birthday_index(friends_collection: collection) -> None:
    """
    Method to create the birthday index and
    notify it is a datetime (not enforce)

    Parameters:
    collection (collection): database collection with all your friends.

    Returns:
    None.
    """
    # Define the index specification
    index_spec = [("birthday", ASCENDING)]

    # Create the index with the partial filter expression
    try:
        friends_collection.create_index(
            index_spec, partialFilterExpression={"birthday": {"$type": "date"}}
        )
        print(f"Index for [{ut.st('cyan', 'birthday')}] created successfully")
    except OperationFailure as e:
        print(ut.st("error", f"Something went wrong creating index.\n{e}"))


def print_indexes(friends_collection: collection) -> None:
    """
    Method to print all the indexes in the collection

    Parameters:
    collection (collection): database collection with all your friends.

    Returns:
    None.
    """
    indexes = friends_collection.list_indexes()
    for index in indexes:
        print(index["name"], "-->", index)


def insert_friend_dict(friends_collection: collection, data: dict) -> None:
    """
    Method to insert a friend directly from raw data

    Parameters:
    collection (collection): database collection with all your friends.
    data (dict): dictionary with all friend data.

    Returns:
    None
    """

    result = friends_collection.insert_one(data)
    # Check if the user has been added
    if result.acknowledged:
        print(
            f"User [name={ut.st('cyan', data['name'])}] "
            f"has been correctly added to the friends_collection."
        )
    else:
        error_msg = (
            f"User [name={data['name']}] has not been added "
            f"to the friends_collection."
        )
        print(ut.st("error", error_msg))


def insert_friend(
    friends_collection: collection,
    name: str,
    birthday: datetime,
    sex: bool,
    alias: str,
    phone: str,
) -> None:
    """
    Method to insert friend data into the collection

    Parameters:
    collection (collection): database collection with all your friends.
    name (str): complete name of the friend you want to retrieve.
    birthday (datetime): birthday of your friend datetime(1978, 6, 23, 0, 0).
    sex (bool): True if male, False if female.
    alias (str): Alias of the friend.
    phone (str): Phone of the friend.

    Returns:
    None.
    """

    birthday, month, month_number, day = ut.check_birthday(birthday)
    user = {
        "name": ut.remove_accents_and_title(name),
        "birthday": birthday,
        "month": month,
        "month_number": month_number,
        "day": day,
        "sex": ut.check_sex(sex),
        "alias": ut.remove_accents_and_title(alias),
        "phone": ut.check_phone(phone),
    }

    result = friends_collection.insert_one(user)
    # Check if the user has been added
    if result.acknowledged:
        print(
            f"User [name={ut.st('cyan', name)}] "
            f"has been correctly added to the friends_collection.\n{user}"
        )
    else:
        error_msg = (
            f"User [name={name}] has not been added to the friends_collection."
        )
        print(ut.st("error", error_msg))


def remove_friend_by_name(friends_collection: collection, name: str) -> None:
    """
    Method to remove a friend by its name.

    Parameters:
    collection (collection): database collection with all your friends.
    name (str): complete name of the friend you want to retrieve.

    Returns:
    None.
    """
    name = ut.remove_accents_and_title(name)
    result = friends_collection.delete_one({"name": name})

    # Check if the document was deleted successfully
    if result.deleted_count == 1:
        print(
            f"Document with [name={ut.st('cyan', name)}] "
            f"deleted successfully."
        )
    else:
        print(ut.st("error", f"Document with [name={name}] not found."))


def update_by_name(
    friends_collection: collection, name: str, field: str, content
) -> None:
    """
    Method to update a field of a friend by its name

    Parameters:
    collection (collection): database collection with all your friends.
    name (str): complete name of the friend you want to retrieve.
    field (str): field to modify.
    content (str): value of the field we want to modify.

    Returns:
    None.
    """
    # Default values
    month, month_number, birthday_day = None, None, None

    # Check the field wanted to update
    field = field.lower()
    if field == "name":
        content = ut.remove_accents_and_title(content)
    elif field == "birthday":
        content, month, month_number, birthday_day = ut.check_birthday(content)
    elif field == "phone":
        content = ut.check_phone(content)
    elif field == "sex":
        content = ut.check_sex(content)
    elif field == "alias":
        content = ut.remove_accents_and_title(content)
    else:
        error_msg = (
            f"Update failed, invalid field [{field}], "
            f"choose one valid [birthday, phone, sex, alias]"
        )
        print(ut.st("error", error_msg))
        exit(1)

    # Homogenize the name
    name = ut.remove_accents_and_title(name)

    # Specify the filter (query) to find the document(s) to update
    filter_query = {"name": name}

    # Specify the update operation
    update_operation = {"$set": {field: content}}

    # Update one document that matches the filter
    update_result = friends_collection.update_one(
        filter_query, update_operation
    )

    # Check if the update was successful
    if not update_result.acknowledged:
        error_msg = (
            f"Something went wrong stablishing the connection"
            f"\n{update_result}"
        )
        print(ut.st("error", error_msg))

    elif update_result.matched_count == 0:
        error_msg = (
            f"Update failed, no documents matched the filter criteria: "
            f"[name={name}]\n{update_result}"
        )
        print(ut.st("error", error_msg))

    elif update_result.modified_count == 1:
        print(
            f"Document [name={ut.st('cyan', name)}] updated successfully: "
            f"[{field}={ut.st('cyan', content)}]"
        )

    elif update_result.modified_count == 0:
        warn_msg = (
            f"Nothing to modify, the document with [name={name}] "
            f"already match the field [{field}={content}]"
        )
        print(ut.st("warn", warn_msg))

    else:
        print(ut.st("error", f"Something went wrong: {update_result}"))

    # If the field is birthday, we need to update more things
    if field == "birthday":
        update_operation2 = {
            "$set": {
                "month": month,
                "month_number": month_number,
                "day": birthday_day,
            }
        }

        # Update one document that matches the filter
        update_result = friends_collection.update_one(
            filter_query, update_operation2
        )

        # Check if the update was successful
        if not update_result.acknowledged:
            error_msg = (
                f"Something went wrong stablishing the "
                f"connection\n{update_result}"
            )
            print(ut.st("error", error_msg))

        elif update_result.matched_count == 0:
            error_msg = (
                f"Update failed, no documents matched "
                f"the filter criteria: [name={name}]\n{update_result}"
            )
            print(ut.st("error", error_msg))

        elif update_result.modified_count == 1:
            month = ut.check_birthday(content)[1]
            print(
                f"Document [name={ut.st('cyan', name)}] updated successfully: "
                f"[month={ut.st('cyan', month)}]"
            )

        elif update_result.modified_count == 0:
            warn_msg = (
                f"Nothing to modify, the document with [name={name}] already "
                f"match the field [month={ut.check_birthday(content)[1]}]"
            )
            print(ut.st("warn", warn_msg))

        else:
            print(ut.st("error", f"Something went wrong: {update_result}"))
