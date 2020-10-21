from bson import ObjectId


class Collection:

    # constructor
    def __init__(self, db, document):
        self._collection = db[document]

    # retrieval functions

    def find_by_criteria(self, criteria: dict) -> list:
        """
        retrieves every entry in the database based on a criteria dictionary
        :param criteria: dictionary of criteria listing
        :rtype list
        :return every element in the database that satisfies the criteria
        """
        ret = []
        coll = self._collection.find(criteria)
        for e in coll:
            ret.append(e)
        return ret

    def find_all(self) -> list:
        """
        retrieves every entry in the database
        :rtype list
        :return every element in the database
        """
        return self.find_by_criteria({})

    def find_by(self, key: str, value: any) -> list:
        """
        find entries based on key-value entry
        :param key: criteria key
        :param value: criteria value
        :rtype list
        :return the entries with the associated criteria
        """
        return self.find_by_criteria({key: value})

    def find_by_object_id(self, _id: str) -> dict:
        """
        find entries if _id is of type ObjectId
        :param _id: string version of object id
        :rtype dict
        :return the entry with the given id
        """
        return self.find_by_id(ObjectId(_id))

    def find_by_id(self, _id: any) -> dict:
        """
        find an entry based on an object id
        :param _id: the id to enter
        :rtype dict
        :return the entry w/ associated id
        """
        tmp = list(self._collection.find({"_id": _id}))
        if len(tmp) == 0:
            return {}
        return tmp[0]

    # insertion functions

    def add(self, entity: dict):
        """
        adds an entry to the database with type ObjectId
        :param entity: the object entity to add
        """
        self._collection.insert_one(entity)

    def add_all(self, entries: list):
        """
        adds multiple entries to the db
        :param entries: the object entity to add
        """
        self._collection.insert_many(entries)

    def add_by_id(self, _id: any, entity: dict):
        """
        adds an entry to the database with a user-defined id
        :param _id: the new id to add
        :param entity: the object entity to add
        :except Exception: general exception
        :raises RuntimeError: error propagated error in try block
        """
        try:
            stub = {'_id': _id}
            stub.update(entity)
            self._collection.insert_one(stub)
        except Exception as e:
            raise RuntimeError(f"Caused by: {e}")

    # removal functions

    def remove_by_id(self, _id: any):
        """
        removes an entry based on id of any type
        :param _id: the object associated with id to remove
        """
        self._collection.delete_one({"_id": _id})

    def remove_by_criteria(self, criteria: dict):
        """
        removes multiple entries if they satisfy a criteria
        :param criteria: specific criteria we want to remove by
        """
        self._collection.delete_many(criteria)

    def clear(self):
        """
        clears all collections in the database
        """
        self.remove_by_criteria({})

    # update functions

    def update_entry(self, _id: any, key: str, value: any, aggregate="set"):
        """
        updates an entries attributes
        :param _id: the id of the entry we want to update
        :param key: attribute name we want to update
        :param value: attribute value mapped from key
        :param aggregate: default set
        https://docs.mongodb.com/manual/reference/operator/aggregation/set/
        """
        if key == "_id":
            raise RuntimeError("You are not allowed to update the object's id")
        curr = self.find_by_id(_id)
        updated = {f"${aggregate}": {key: value}}
        self._collection.update_one(curr, updated)

    # properties functions

    def size(self) -> int:
        """
        size of collection
        :rtype int
        :return number of elements in the collection
        """
        return self._collection.count_documents({})

    def empty(self) -> bool:
        """
        sees if collection is empty
        :rtype bool
        :return: true if size is equal to 0
        """
        return self.size() == 0

    def contains_id(self, _id: any) -> bool:
        """
        checks if the collection contains an element based on id
        :param _id: the id to search for
        :rtype bool
        :return true if can find by id
        """
        return len(self.find_by_id(_id)) > 0

    def contains_entry(self, entry: dict) -> bool:
        """
        checks if the collection contains an element
        :param entry: what to search for
        :rtype bool
        :return true if can find by entry that contains criteria
        """
        return len(self.find_by_criteria(entry)) > 0
