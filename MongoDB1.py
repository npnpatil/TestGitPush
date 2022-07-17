import pymongo
client = pymongo.MongoClient("mongodb+srv://npnpatil:Nitin12345@nitin.0zbrx.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


d = {"name":"Nitin", "email":"npnpatil@gmail.com", "surname":"Patil"}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)