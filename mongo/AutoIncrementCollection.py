from Collection import *


# uses auto-increment to generate the id
class AutoIncrementCollection(Collection):

    # helper functions
    def __probe(self, _id: int):
        count = 0
        while self.contains_id(_id + count):
            count = count + 1
        return count

    # constructor
    def __init__(self, db, document):
        super().__init__(db, document)

    '''
    Method Not allowed
    '''
    def find_by_object_id(self, _id: str):
        raise RuntimeError("Method not allowed for auto-inc databases!")

    '''
    find an entry based on the integer id
    @param id: the id to enter
    @return the entry w/ associated id
    '''
    def find_by_id(self, _id: int):
        return super().find_by_id(int(_id))

    # insertion functions

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
        super().remove_by_id(int(_id))

    '''
    updates an entries attributes
    @param _id: the id as an int of the entry we want to update
    @key: attribute name we want to update
    @value: attribute value mapped from key
    @aggregate: default set
    https://docs.mongodb.com/manual/reference/operator/aggregation/set/
    '''
    def update_entry(self, _id: int, key: str, value: any, aggregate="set"):
        super().update_entry(int(_id), key, value, aggregate)

    """
    checks if the collection contains an element based on an int id
    @parm id: the id to search for
    @return true if can find by id
    """
    def contains_id(self, _id: int):
        return len(self.find_by_id(_id)) > 0
