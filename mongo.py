import pymongo

connection = pymongo.MongoClient("homer.stuy.edu")

db = connection.test

col = db.restaurants

print col.find({}).count()

def print_cursor(cursor):
	for d in cursor:
		print d['name']

def find_borough(bor):
	cursor = col.find({
		"borough": bor
	})
	print_cursor(cursor)

def find_zip(zipcode):
	cursor = col.find({
		"address.zipcode": zipcode
	})
	print_cursor(cursor)

def find_zip_grade(zipcode, grade):
	print_cursor(
	col.find({
		"address.zipcode": zipcode,
		"grades.grade": grade
	})
	)

def find_zip_score(zipcode, score):
	print_cursor(
	col.find({
		"address.zipcode": zipcode,
		"grades.score": {
			"$lt": score
		}
	})
	)

def find_restaurant(res):
	print_cursor(db.restaurants.find({name: {'$regex': res}}))


find_borough("Bronx")
find_zip("11209")
find_zip_grade("11209", "A")
find_zip_score("11209", 11)
find_restaurant("Delic")

connection.close()
