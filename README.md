<img src="mongo.png" height = 100>

## How to Install

1. Follow the <a href="https://www.mongodb.com/try/download/enterprise">MongoDB  link</a>
2. choose your OS
3. Select the latest version
4. Click 'Download'
5. Follow the steps in the set up wizard 
    - make sure "Install MongoDB Compass" is checked
<img src = "mongo_install.jpg">

## MongoDB Shell

##### Install 
```bash
$ sudo apt install mongodb
```

##### Launch Mongo Shell
Using the default host and port
- {host} => custom host
- {port} => custom port
```bash
$ mongo 
```

Using a custom host and port
```bash
$ mongo {host}:{port} 
```

Connect Remote:
- {username} => your mongoDB username
- {server} => your mongoDB cluster
```bash
$ mongo "mongodb+srv://{server}/{dbname}" --username {username}
```

##### Finding and Selecting Databases and Collections
Show all databases
```bash
> show dbs
```

select a database
- {database} => database you want to use
```bash
> use {database}
```

##### Basic Operations
- {collection} => the collection you want to use
- to specify a criteria, use JSON notation
- {} => refers to all documents
```bash
> db.{collection}.find({}) # find all documents
> db.{collection}.find({"CS industry":"data science"}) # find all documents with the given criteria

> db.{collection}.insertOne({"game":"fortnite"}) # insert 1 element
> db.{collection}.insertOne([{"game":"fortnite"}, {"game":"angry birds"}]) # insert multiple elements (NEEDS TO BE AN ARRAY)

> db.{collection}.deleteOne({"language":"sql"}) # delete the first element with a matching criteria
> db.{collection}.deleteMany({"subject":"research"}) # delete all elements with a matching criteria
> db.{collection}.deleteMany({}) # clears all the documents in the db

# 1st argument: criteria
# 2nd argument: update to
# updateOne(<CRITERIA>, {$set:<NEW ENTRY>})
> db.{collection}.updateOne({"name":"omruti"}, {$set:{"loves":"fortnite"}}) # update one 
```