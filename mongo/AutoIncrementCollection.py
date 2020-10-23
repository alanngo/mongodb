from Collection import *

_OBJ_ID_ERR = "Method not allowed for auto-inc document!"


# uses auto-increment to generate the id
class AutoIncrementCollection(Collection):

    # helper functions
    def __probe(self, _id: int) -> int:
        count = 0
        while self.contains_id(_id + count):
            count = count + 1
        return count

    # constructor
    def __init__(self, db, document):
        super().__init__(db, document)

    def find_by_id(self, _id: int) -> dict:
        """
        find an entry based on the integer id
        :param _id: the id to enter
        :rtype dict
        :return the entry w/ associated id
        """
        return super().find_by_id(int(_id))

    # insertion functions

    def add(self, entity: dict):
        """
        adds an entry to the database by auto-incrementing
        :param entity: the object entity to add
        """
        if self.empty():
            self.add_by_id(1, entity)
        else:
            index = self.size()
            offset = self.__probe(index)
            self.add_by_id(index + offset, entity)

    def add_all(self, entries: list):
        """
        adds multiple entries to the db
        :param entries: the object entity to add
        """
        for e in entries:
            self.add(e)

    # removal functions

    def remove_by_id(self, _id: int):
        """
        removes an entry based on an id of int type
        :param _id: the object associated with id to remove
        """
        super().remove_by_id(int(_id))

    def update_by_id(self, _id: int, key: str, value: any, aggregate="set"):
        """
        updates an entries attributes
        :param _id: the id as an int of the entry we want to update
        :param key: attribute name we want to update
        :param value: attribute value mapped from key
        :param aggregate: default set

        https://docs.mongodb.com/manual/reference/operator/aggregation/set/
        """
        super().update_by_id(int(_id), key, value, aggregate)

    def contains_id(self, _id: int) -> bool:
        """
        checks if the collection contains an element based on an int id
        :param _id: the id to search for
        :rtype bool
        :return True if can find by id
        """
        return len(self.find_by_id(_id)) > 0

    # methods not allowed because Auto Inc does not support ObjectId
    def find_by_object_id(self, _id: str):
        raise RuntimeError(_OBJ_ID_ERR)

    def remove_by_object_id(self, _id: str):
        raise RuntimeError(_OBJ_ID_ERR)

    def update_by_object_id(self, _id: str, key: str, value: any, aggregate="set"):
        raise RuntimeError(_OBJ_ID_ERR)

    def contains_object_id(self, _id: str) -> bool:
        raise RuntimeError(_OBJ_ID_ERR)
