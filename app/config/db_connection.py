from pymongo import MongoClient

mongo_url: str = "mongodb+srv://brayhanstiv:TBOCOtUtGXYREOqp@cluster0.zy1lp4o.mongodb.net/bank"

client = MongoClient(mongo_url)

database = client.bank
vendor_collection = database.vendors
debt_collection = database.debts
payment_history_collection = database.payments_history