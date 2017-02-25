import pymongo

__author__ = 'Prajesh Ananthan'


class Database(object):
    URI = "mongodb://127.9.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialize():
        database_name = 'fullstack'
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client[database_name]

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, data):
        Database.DATABASE[collection].find(data)

    @staticmethod
    def find_one(collection, data):
        Database.DATABASE[collection].find_one(data)
