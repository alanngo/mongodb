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
# a). set up mongodb connection by specifing url
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
- find_by_id(id: int): dict 
- add(entity: dict)
- add_all(entries: list)
- remove_by_id(id: int)
- clear()
- update_entry(id: int, key: str, value: any, aggregate="set")
- size(): int
- empty(): bool
- contains_id(id: int): bool
- contains_entry(entry: dict): bool

# use cautiously
- default_add(entity: dict) 
- add_by_id(id: any, entity: dict)
```