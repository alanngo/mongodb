from pymongo import *

from .AutoIncrementCollection import *
from .ObjectIdCollection import *
from .Collection import *

DEFAULT = 0
AUTO_INCREMENT = 1
OBJECT_ID = 2


class MongoDB:

    # constructor
    def __init__(
            self,
            database: str,
            docs: dict,
            url: str = None,
            host: str = None,
            port: int = None,

    ):
        """
        :param database: database name to use
        :param docs: collections in the database
        :param url: mongodb url
        :param host: connection host
        :param port: connection port
        :raises RuntimeError: raised in the following cases
                - host/port specified w/o port/host
                - url specified w/ host and/or port
        """
        if host is None and port is None and url is None:
            cluster = MongoClient("localhost", 27017)  # default connection
        elif (host is not None and port is not None) and (url is None):
            cluster = MongoClient(host, port)  # user-specified connection
        elif (host is None and port is None) and (url is not None):
            cluster = MongoClient(url)  # cluster connection
        else:
            raise RuntimeError("USAGE:\n"
                               "mongo = MongoDB(host=HOST, port=PORT, database=DATABASE, docs=COLLECTION)\n"
                               "or\n"
                               "mongo = MongoDB(url=URL, database=DATABASE, docs=COLLECTION)")
        db = cluster[database]
        self.collection = {}
        for k in docs:  # k -> collection name
            if docs[k] == DEFAULT:
                self.collection[k] = Collection(db, k)
            if docs[k] == AUTO_INCREMENT:
                self.collection[k] = AutoIncrementCollection(db, k)
            if docs[k] == OBJECT_ID:
                self.collection[k] = ObjectIdCollection(db, k)
