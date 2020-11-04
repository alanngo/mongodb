from pymongo import *

from .AutoIncrementCollection import *
from .ObjectIdCollection import *
from .Collection import *
from .MongoError import *

DEFAULT = 0
AUTO_INCREMENT = 1
OBJECT_ID = 2


# MongoDB Wrapper Class
class MongoDB:

    # constructor
    def __init__(
            self,
            database: str,
            collections: dict,
            url: str = None,
            host: str = None,
            port: int = None,

    ):
        """
        :param database: database name to use
        :param collections: collections in the database
        :param url: mongodb url
        :param host: connection host
        :param port: connection port
        :raises MongoError: raised in the following cases
                - host/port specified w/o port/host
                - url specified w/ host and/or port
        """
        if host is None and port is None and url is None:
            connection = MongoClient("localhost", 27017)  # default connection
        elif (host is not None and port is not None) and (url is None):
            connection = MongoClient(host, port)  # user-specified connection
        elif (host is None and port is None) and (url is not None):
            connection = MongoClient(url)  # url-based connection
        else:
            raise MongoError("USAGE:\n"
                             "mongo = MongoDB(database=DATABASE, collections=COLLECTION)\n"
                             "or\n"
                             "mongo = MongoDB(host=HOST, port=PORT, database=DATABASE, collections=COLLECTION)\n"
                             "or\n"
                             "mongo = MongoDB(url=URL, database=DATABASE, collections=COLLECTION)")
        db = connection[database]
        self.collection = {}
        for k in collections:  # k -> collection name
            if collections[k] == DEFAULT:
                self.collection[k] = Collection(db, k)
            if collections[k] == AUTO_INCREMENT:
                self.collection[k] = AutoIncrementCollection(db, k)
            if collections[k] == OBJECT_ID:
                self.collection[k] = ObjectIdCollection(db, k)
