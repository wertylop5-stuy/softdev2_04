import pymongo

connection = pymongo.MongoClient("homer.stuy.edu")

db = connection.KS

col = db.data

filename = "data.json"
file = open(filename, "r")

for x in file:
    print x
    break
file.close()
