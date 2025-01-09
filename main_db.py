import os  # noqa: F401 pylint: disable=unused-import
from datetime import datetime  # noqa: F401 pylint: disable=unused-import

from pymongo import MongoClient

from mongodb import filters as f  # noqa: F401 pylint: disable=unused-import
from mongodb import (  # noqa: F401 pylint: disable=unused-import
    internal_queries as q,
)
from utils import utilities as ut  # noqa: F401 # pylint: disable=unused-import

############################## MAIN OF MONGODB ################################
# This main is an example of how to use mongodb module
###############################################################################

# Get MongoDB connection details from environment variables
mongo_host = os.getenv("MONGO_HOST", "localhost")
mongo_port = int(os.getenv("MONGO_PORT", "27017"))

# Defining database
client = MongoClient(mongo_host, mongo_port)
db = client["friends_birthdays"]
friends_collection = db["friends_collection"]

# Execute here your query
print(f.get_birthdays_by_month(friends_collection, "january")
