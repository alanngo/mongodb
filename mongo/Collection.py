# 1 collection in a database
class Collection:

    # helper functions
    def __probe(self, id):
        count = 0
        while len(self.find_by_id(id + count)) > 0:
            count = count + 1
        return count

    # constructor
    def __init__(self, db, document):
        self.__collection = db[document]

    # retrieval functions

    """
    retrieves every entry in the database based on a criteria dictionary
    @parm criteria: dictionary of criteria listing
    @return every element in the database that satisfies the criteria
    """
    def find_by_criteria(self, criteria: dict):
        ret = []
        coll = self.__collection.find(criteria)
        for e in coll:
            ret.append(e)
        if len(ret) == 1:
            return ret[0]
        return ret

    """
    retrieves every entry in the database
    @return every element in the database
    """
    def find_all(self):
        return self.find_by_criteria({})

    '''
    find entries based on key-value entry
    @param key: criteria key
    @param value: criteria value
    @return the entries with the associated criteria
    '''
    def find_by(self, key, value: any):
        return self.find_by_criteria({key: value})

    '''
    find an entry based on the id
    @param id: the id to enter
    @return the entry w/ associated id
    '''
    def find_by_id(self, id):
        return self.find_by("_id", int(id))

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
        except Exception:
            raise RuntimeError(f"Duplicate keys detected: {id}")

    '''
    adds an entry to the database by auto-incrementing
    @param entity: the object entity to add
    '''
    def add(self, entity: dict):
        index = self.size() + 1
        offset = self.__probe(index)
        self.add_by_id(index + offset, entity)

    '''
    adds multiple entries to the db
    @param entity: the object entity to add
    '''
    def add_all(self, entries):
        for e in entries:
            self.add(e)

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
        self.__collection.delete_many({})

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
        if key == "_id":
            raise RuntimeError("You are not allowed to update the object's id")
        curr = self.find_by_id(id)
        updated = {f"${aggregate}": {key: value}}
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

    """
    checks if the collection contains an element based on id
    @parm id: the id to search for
    @return true if can find by id
    """
    def contains_id(self, id):
        return len(self.find_by_id(id)) > 0

    """
    checks if the collection contains an element
    @parm entry: what to search for
    @return true if can find by entry that contains criteria
    """
    def contains_entry(self, entry: dict):
        return len(self.find_by_criteria(entry)) > 0
