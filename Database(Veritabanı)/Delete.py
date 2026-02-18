import pymongo
from bson.objectid import ObjectId
from pymongo.collation import Collation



myclient = pymongo.MongoClient("mongodb://localhost:27017/")


mydb = myclient["yarisciler"]






mycollection = mydb["taylar"]














x = mycollection.delete_one({"jokey":{"$regex":"^A"}})
    
        
    
        
           
            
    
print(f"{x.deleted_count} kayıt silindi.....")



    




for i in mycollection.find():
    print(i)
