# 使用mongodb储存爬取的数据
https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/
## Installation
+ Tap the MongoDB Homebrew Tap to download the official Homebrew formula for MongoDB and the Database Tools, by running the following command in your macOS Terminal: 
```
brew tap mongodb/brew
```
+ To update Homebrew and all existing formulae:
```
brew update
```
+ To install MongoDB, run the following command in your macOS Terminal application:
```
brew install mongodb-community@5.0
```
## Run MongoDB Community Edition
+ To run MongoDB (i.e. the mongod process) as a macOS service, run:
```
brew services start mongodb-community@5.0
```
+ To stop a mongod running as a macOS service, use the following command as needed:
```
brew services stop mongodb-community@5.0
```
+ To run MongoDB (i.e. the mongod process) manually as a background process, run:
```
mongod --config /usr/local/etc/mongod.conf --fork
```
## Connect and Use MongoDB
+ To begin using MongoDB, connect mongosh to the running instance. From a new terminal, issue the following:
```
mongosh
```
### mongosh commands
To list the databases available to the user, use the helper 
```
show dbs
```
To switch databases
```
use <db>
```
Read All Documents in a Collection
```
db.items.find()
```
Count the entries. Use countDocuments or estimatedDocumentCount.
```
db.items.countDocuments()
```
Update item
To update the first document in the sample_mflix.movies collection where title equals "Tag":

```
db.movies.updateOne( { title: "Tag" },
{
  $set: {
    plot: "One month every year, five highly competitive friends
           hit the ground running for a no-holds-barred game of tag"
  }
  { $currentDate: { lastUpdated: true } }
})
```

Find one item
Returns one document that satisfies the specified query criteria on the collection or view. If multiple documents satisfy the query, this method returns the first document according to the natural order which reflects the order of documents on the disk. In capped collections, natural order is the same as insertion order. If no document satisfies the query, the method returns null.
```
db.urls.findOne()
```
For more documentation of basic MongoDB operations in mongosh, see:
+ https://www.mongodb.com/docs/mongodb-shell/crud/insert/
+ https://www.mongodb.com/docs/mongodb-shell/crud/read/
+ https://www.mongodb.com/docs/mongodb-shell/crud/update/
+ https://www.mongodb.com/docs/mongodb-shell/crud/delete/

安装mongodb
https://www.runoob.com/python3/python-mongodb.html
```
pip3 install pymongo
```

export mongodb
https://www.mongodb.com/docs/database-tools/mongoexport/  
```
mongoexport --collection=items --db=mongotest --out=items.json
```

import mongodb
https://www.mongodb.com/docs/database-tools/mongoimport/
```
mongoimport --db=mongotest --collection=items mongodb://localhost:27017/ --file=items.json
```