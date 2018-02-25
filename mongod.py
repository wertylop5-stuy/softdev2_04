'''
Current US Representatives: a list of all the state representatives currently serving
in Congress.

Download: https://www.govtrack.us/api/v2/role?current=true&role_type=representative&limit=438

We went through every element in the list "objects" and inserted
those into the database.
'''

import pymongo
import json

connection = pymongo.MongoClient("homer.stuy.edu")

db = connection.KS

col = db.data

filename = "data.json"
file = open(filename, "r")

js = json.load(file)

#Inserts the data into the db
'''
for x in js['objects']:
    col.insert_one(x);
'''

def print_cursor(cursor):
    for d in cursor:
            print d

def find_party(party):
    cursor = col.find({
        "party": party
    })
    print_cursor(cursor)

def find_person(last, first):
    cursor = col.find({
        "person.lastname": last,
        "person.firstname": first
    })
    print_cursor(cursor)

def find_twitter(twitter_id):
    cursor = col.find({
        "person.twitterid": twitter_id
    })
    print_cursor(cursor)

def find_state(state_code):
    print_cursor(
        col.find({
            "state": state_code
        })
    )


#find_party("Republican")
#find_person("Aderholt", "Robert")
#find_twitter("Robert_Aderholt")
find_state("AL")

connection.close()
file.close()
