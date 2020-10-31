from .Collection import *
from bson import ObjectId


class ObjectIdCollection(Collection):
    # constructor
    def __init__(self, db, document):
        super().__init__(db, document)

    def find_by_id(self, _id: any) -> dict:
        """
        find entry w/ _id  of type ObjectId
        :param _id: string version of object id
        :rtype dict
        :return the entry with the given id
        """
        return super().find_by_id(ObjectId(_id))

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

    def remove_by_id(self, _id: str):
        """
        removes an entry based on id of type ObjectId
        :param _id: ObjectId type _id
        """
        super().remove_by_id(ObjectId(_id))

    def update_by_id(self, _id: str, key: str, value: any, aggregate=SET):
        """
        updates an entries attributes by finding the entry w/ matching id
        :param _id: the id of the entry we want to update
        :param key: attribute name we want to update
        :param value: value to update to/by
        :param aggregate: default set
        https://docs.mongodb.com/manual/reference/operator/aggregation/set/
        """
        super().update_by_id(ObjectId(_id), key, value, aggregate)

    def contains_id(self, _id: str) -> bool:
        """
        checks if the collection contains an element based on id of type ObjectId
        :param _id: the id to search for
        :rtype bool
        :return true if can find by id
        """
        return len(self.find_by_id(_id)) > 0
