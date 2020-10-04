# 1 collection in a database
class Collection:

    # helper functions
    def __probe(self, _id: int):
        count = 0
        while self.contains_id(_id + count):
            count = count + 1
        return count

    # constructor
    def __init__(self, db, document):
        self.__collection = db[document]

    ##########################################################
    # DEFAULT FUNCTIONS: use ONLY if id is NOT int type
    '''
    find an entry based on an object id
    @param id: the id to enter
    @return the entry w/ associated id
    '''
    def default_find_by_id(self, _id: any):
        tmp = self.find_by("_id", _id)
        if len(tmp) == 0:
            return {}
        return tmp[0]

    '''
    adds an entry to the database with a auto-generated id
    @param entity: the object entity to add
    '''
    def default_add(self, entity: dict):
        self.__collection.insert_one(entity)

    '''
    removes an entry based on id of any type
    @param id: the object associated with id to remove
    '''
    def default_remove_by_id(self, _id: any):
        self.__collection.delete_one({"_id": _id})

    """
    checks if the collection contains an element based on id
    @parm id: the id to search for
    @return true if can find by id
    """
    def default_contains_id(self, _id: any):
        return len(self.default_find_by_id(_id)) > 0

    ##########################################################

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
    find an entry based on the integer id
    @param id: the id to enter
    @return the entry w/ associated id
    '''
    def find_by_id(self, _id: int):
        return self.default_find_by_id(int(_id))

    # insertion functions

    '''
    adds an entry to the database with a user-defined id
    @param id: the new id to add
    @param entity: the object entity to add
    '''
    def add_by_id(self, _id: any, entity: dict):
        try:
            stub = {'_id': _id}
            stub.update(entity)
            self.default_add(stub)
        except Exception as e:
            raise RuntimeError(f"Caused by: {e}")

    '''
    adds an entry to the database by auto-incrementing
    @param entity: the object entity to add
    '''
    def add(self, entity: dict):
        if self.empty():
            self.add_by_id(1, entity)
        else:
            index = self.size()
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
    removes an entry based on an id of int type
    @param id: the object associated with id to remove
    '''
    def remove_by_id(self, _id: int):
        self.default_remove_by_id(int(_id))

    '''
    removes multiple entries if they satisfy a criteria
    @param criteria: specific criteria we want to remove by
    '''
    def remove_by_criteria(self, criteria: dict):
        self.__collection.delete_many(criteria)

    '''
    clears all collections in the database
    '''
    def clear(self):
        self.remove_by_criteria({})

    # update functions

    '''
    updates an entries attributes
    @param id: the id of the entry we want to update
    @key: attribute name we want to update
    @value: attribute value mapped from key
    @aggregate: default set
    https://docs.mongodb.com/manual/reference/operator/aggregation/set/
    '''
    def update_entry(self, _id: any, key: str, value: any, aggregate="set"):
        if key == "_id":
            raise RuntimeError("You are not allowed to update the object's id")
        curr = self.default_find_by_id(_id)
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
    checks if the collection contains an element based on an int id
    @parm id: the id to search for
    @return true if can find by id
    """
    def contains_id(self, _id: int):
        return len(self.find_by_id(_id)) > 0

    """
    checks if the collection contains an element
    @parm entry: what to search for
    @return true if can find by entry that contains criteria
    """
    def contains_entry(self, entry: dict):
        return len(self.find_by_criteria(entry)) > 0
