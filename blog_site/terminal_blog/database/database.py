import pymongo

__author__ = 'Prajesh Ananthan'


class Database(object):
    URI = "mongodb://127.0.0.1:27017"
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
    def find(collection, query):
        result = Database.DATABASE[collection].find(query)
        return result

    @staticmethod
    def find_one(collection, query):
        result = Database.DATABASE[collection].find_one(query)
        return result
