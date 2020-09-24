from mongo.MongoDB import *

PASSWORD = "6627 56837 73732724"
DATABASE = "dealership"
COLLECTIONS = ["car", "dealer"]
URL = f"mongodb+srv://alan:{PASSWORD}@cluster0.u6lhh.mongodb.net/{DATABASE}?retryWrites=true&w=majority"

mongo = MongoDB(database=DATABASE, docs=COLLECTIONS, url=URL)
car = mongo.collection["car"]
dealer = mongo.collection["dealer"]

cars = \
    [
        {"make": "honda", "model": "civic", "year": 2001},
        {"make": "toyota", "model": "camry", "year": 2005},
    ]

dealers = \
    [
        {"name": "varshika", "age": 23, "loves": ["sleeping", "watching tv"]},
        {"name": "smruti", "age": 20, "loves": ["bubble tea", "beer", "sleeping"]},
        {"name": "angela", "age": 21, "loves": ["python", "books"]},
        {"name": "omar", "age": 25, "loves": ["sql", "shell scripts", "research", "flask"]}
    ]


def main():
    for d in dealers:
        dealer.add(d)
    for c in cars:
        car.add(c)


main()
