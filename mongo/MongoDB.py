from pymongo import *

from mongo.Collection import Collection


class MongoDB:

    # constructor
    def __init__(
            self,
            database: str,
            docs: list,
            url: str = None,
            host: str = None,
            port: int = None
    ):

        if host or port is not None:
            cluster = MongoClient(host, port)
        else:
            cluster = MongoClient(url)
        db = cluster[database]
        self.collection = {}
        for doc in docs:
            self.collection[doc] = Collection(db, doc)
