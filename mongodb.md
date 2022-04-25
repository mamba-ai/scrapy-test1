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
安装mongodb
https://www.runoob.com/python3/python-mongodb.html
```
pip3 install pymongo
```