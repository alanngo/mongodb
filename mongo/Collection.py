from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError


# 1 collection in a database
class Collection:

    # helper functions
    def __probe(self, id):
        count = 0
        while len(self.find_by_id(id + count)) > 0:
            count = count + 1
        return count

    def __init__(self, db, document):

        # if host or port is not None:
        #     cluster = MongoClient(host, port)
        # else:
        #     cluster = MongoClient(url)
        # db = cluster[database]
        self.__collection = db[document]

    # retrieval functions

    """
    retrieves every entry in the database
    @return every element in the database
    """

    def find_all(self):
        ret = []
        coll = self.__collection.find({})
        for e in coll:
            ret.append(e)
        return ret

    '''
    find entries based on criteria
    @param key: criteria key
    @param value: criteria value
    @return the entries with the associated criteria
    '''

    def find_by_criteria(self, key, value):
        coll = self.__collection.find({key: value})
        ret = []
        for e in coll:
            ret.append(e)
        if len(ret) == 1:
            return ret[0]
        return ret

    '''
    find an entry based on the id
    @param id: the id to enter
    @return the entry w/ associated id
    '''

    def find_by_id(self, id):
        ret = self.find_by_criteria("_id", int(id))
        return ret

    # insertion functions

    '''
    adds an entry to the database with a auto-generated id
    @param entity: the object entity to add
    '''

    def default_add(self, entity: dict):
        self.__collection.insert_one(entity)

    '''
    adds an entry to the database with a user-defined id
    @param id: the new id to add
    @param entity: the object entity to add
    '''

    def add_by_id(self, id, entity: dict):
        try:
            stub = {'_id': id}
            stub.update(entity)
            self.default_add(stub)
        except DuplicateKeyError:
            raise RuntimeError(f"Duplicate keys detected: {id}")

    '''
    adds an entry to the database by auto-incrementing:wq
    @param entity: the object entity to add
    '''

    def add(self, entity: dict):
        index = self.size() + 1
        offset = self.__probe(index)
        self.add_by_id(index + offset, entity)

    # removal functions

    '''
    removes an entry based on an id
    @param id: the object associated with id to remove
    '''

    def remove_by_id(self, id):
        self.__collection.delete_one({"_id": int(id)})

    '''
    clears all collections in the database
    '''

    def clear(self):
        self.__collection.drop()

    # update functions

    '''
    updates an entries attributes
    @param id: the id of the entry we want to update
    @key: attribute name we want to update
    @value: attribute value mapped from key
    @aggregate: default set
    https://docs.mongodb.com/manual/reference/operator/aggregation/set/
    '''

    def update_entry(self, id, key: str, value: any, aggregate="set"):
        curr = self.find_by_id(id)
        updated = {"$" + aggregate: {key: value}}
        self.__collection.update_one(curr, updated)

    # properties functions

    '''
    size of collection
    @return number of elements in the collection
    '''

    def size(self):
        return self.__collection.count_documents({})

    '''
    sees if collection is empty
    @return: true if size is equal to 0
    '''

    def empty(self):
        return self.size() == 0
