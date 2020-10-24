from MongoDB import *

DATABASE = "UnitTestDB"
COLLECTION = {"TestCollection": AUTO_INCREMENT, "TestCollection2": DEFAULT}
HOST = "localhost"
PORT = 27017
URL = f"mongodb+srv://alan:2526@cluster0.u6lhh.mongodb.net/{DATABASE}?retryWrites=true&w=majority"
MONGO1 = MongoDB(database=DATABASE, docs=COLLECTION)
print("mongo1")
MONGO2 = MongoDB(host=HOST, port=PORT, database=DATABASE, docs=COLLECTION)
print("mongo2")
# MONGO3 = MongoDB(url=URL, database=DATABASE, docs=COLLECTION)
# print("mongo3")
# MONGO4 = MongoDB(host=HOST, database=DATABASE, docs=COLLECTION)
# print("mongo4")
a = MONGO1.collection["TestCollection"]
b = MONGO2.collection["TestCollection2"]
a.clear()
b.clear()
li = [{"name": "smruti"}, {"name": "anusha"}]

a.add_all(li)
b.add_all(li)
print(b.size())
print(b.find_all())
print(a.size())
a.update_entry(criteria={"name": "smruti"}, key="hobby", value="coffee")
a.update_by_id(2, key="hobby", value=["dancing", "business stuff", "SWE"])
a.update_all(key="classes", value=["OS", "Algo", "SWE"])
a.update_entries({"classes": ["OS", "Algo", "SWE"]}, key="school", value="UT Austin")
print(a.find_all())
# print(b.find_by_object_id("5f8f853c2af277e270fac3a9"))
print("done")
