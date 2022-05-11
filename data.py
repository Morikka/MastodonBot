import pymongo
from pymongo import MongoClient
import random

def connect():
    myclient = MongoClient("mongodb://localhost:27017/")
    db = myclient["retirebot"] # Database
    collection = db["myCollection"]
    return collection
    

def GetData():
    collection = connect()
    rand = random.randint(3, 5)
    res = collection.aggregate([{"$sample": {"size": rand}}])
    return list(res)

def GenerateMessage():
    msg = GetData()
    res = ""
    do = ""
    donot = ""
    for item in msg:
        rand = random.random()
        if(rand<0.5):
            l = random.randint(0, len(item['do'])-1)
            do += item['name'] + ": " + item['do'][l] + '\n'
        else:
            l = random.randint(0, len(item['donot'])-1)
            donot += item['name'] + ": " + item['donot'][l] + '\n'
    if(do==""):
        do = "今日宜：今日诸事不宜" + '\n'
    else: 
        do = "今日宜:" + '\n' + do
    if(donot==""):
        donot += "今日不宜：今日诸事顺利" + '\n'
    else: 
        donot = "今日不宜:" + '\n'  + donot
    res = ":EveOneCat23: 快来查看专属于打工人的今日运势吧 :EveOneCat23: " + '\n\n' + do + '\n' + donot
    return res
    
if __name__ == "__main__":
    res = GenerateMessage()
    print(res)

