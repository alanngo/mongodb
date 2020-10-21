from pymongo import *

from AutoIncrementCollection import *
from Collection import *

DEFAULT = 0
AUTO_INCREMENT = 1


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

        if host or port is not None:
            cluster = MongoClient(host, port)
        else:
            cluster = MongoClient(url)
        db = cluster[database]
        self.collection = {}
        for k in docs:  # k -> collection name
            if docs[k] == DEFAULT:
                self.collection[k] = Collection(db, k)
            if docs[k] == AUTO_INCREMENT:
                self.collection[k] = AutoIncrementCollection(db, k)
