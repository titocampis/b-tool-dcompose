from pymongo import ASCENDING
from pymongo.errors import OperationFailure

import utils.utilities as ut


def create_birthday_index(collection):
    """
    Method to create the birthday index and
    notify it is a datetime (not enforce)
    """
    # Define the index specification
    index_spec = [("birthday", ASCENDING)]

    # Create the index with the partial filter expression
    try:
        collection.create_index(
            index_spec, partialFilterExpression={"birthday": {"$type": "date"}}
        )
        print(f"Index for [{ut.st('cyan', 'birthday')}] created successfully")
    except OperationFailure as e:
        print(ut.st("error", f"Something went wrong creating index.\n{e}"))


def get_indexes(collection):
    """Method to return all the indexes in the collection"""
    indexes = collection.list_indexes()
    for index in indexes:
        print(index["name"], "-->", index)


def insert_friend_dict(collection, data):
    """Method to insert a friend directly from raw data"""

    result = collection.insert_one(data)
    # Check if the user has been added
    if result.acknowledged:
        print(
            f"User [name={ut.st('cyan', data['name'])}] "
            f"has been correctly added to the collection."
        )
    else:
        error_msg = (
            f"User [name={data['name']}] has not been added to the collection."
        )
        print(ut.st("error", error_msg))


def insert_friend(collection, name, birthday, sex, alias, phone):
    """Method to insert friend data into the collection"""

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

    result = collection.insert_one(user)
    # Check if the user has been added
    if result.acknowledged:
        print(
            f"User [name={ut.st('cyan', name)}] "
            f"has been correctly added to the collection.\n{user}"
        )
    else:
        error_msg = f"User [name={name}] has not been added to the collection."
        print(ut.st("error", error_msg))


def remove_friend_by_name(collection, name):
    """Method to remove a friend by its name"""
    name = ut.remove_accents_and_title(name)
    result = collection.delete_one({"name": name})

    # Check if the document was deleted successfully
    if result.deleted_count == 1:
        print(
            f"Document with [name={ut.st('cyan', name)}] "
            f"deleted successfully."
        )
    else:
        print(ut.st("error", f"Document with [name={name}] not found."))


def update_by_name(collection, name, field, content):
    """Method to update a field of a friend by its name"""
    # Default values
    content, month, month_number, birthday_day = None, None, None, None

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
    update_result = collection.update_one(filter_query, update_operation)

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
            f"Document [{ut.st('cyan', f'name={name}')}] updated successfully: "
            f"[{ut.st('cyan', f'{field}={content}')}]"
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
        update_result = collection.update_one(filter_query, update_operation2)

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
