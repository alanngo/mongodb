# MongoDB Helper Class
- Used to do heavy lifting for mongo operations
- Utilizes 'pymongo' library
- Make sure you copy this directory in the described structure below to your python workspace
    - mongo/Collection.py
    - mongo/MongoDB.py
- This class uses auto-increment to generate the id

###### Initialization
```python
# PICK ONE
# a). set up mongodb connection by specifying url
mongo = MongoDB(
    database=DATABASE, # the database name you want to use 
    docs=COLLECTIONS,  # collections you want to store in the db
    url=URL # mongodb or localhost url
    )

# b). set up mongodb connection by defining host and port
mongo = MongoDB(
    database=DATABASE, # the database name you want to use  
    docs=COLLECTIONS, # collections you want to store in the db
    host=HOST, # server host
    port=PORT # server port
    )

# define your collections
coll = mongo.collection[COLLECTION_NAME]
...

# you are all set with the initialization step
```

###### Functionality
```python
# Look in Collection.py for more info

# useful functions
- find_by_criteria(criteria: dict): list 
- find_all(): list 
- find_by(key: str value: any): list 
- find_by_id(_id: int): dict 
- add_by_id(_id: any, entity: dict)
- add(entity: dict)
- add_all(entries: list)
- remove_by_id(_id: int)
- remove_by_criteria(criteria: dict)
- clear()
- update_entry(_id: any, key: str, value: any, aggregate="set")
- size(): int
- empty(): bool
- contains_id(_id: int): bool
- contains_entry(entry: dict): bool

# use if id is NOT of type int
- default_find_by_id(_id: any): dict
- default_add(entity: dict) 
- default_remove_by_id(_id: any)
- default_contains_id(_id: any): bool
```
