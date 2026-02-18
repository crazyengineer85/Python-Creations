import pymongo
from bson.objectid import ObjectId
from pymongo.collation import Collation



myclient = pymongo.MongoClient("mongodb://localhost:27017/")


mydb = myclient["yarisciler"]






mycollection = mydb["taylar"]


# mycollection.update_one (
    
        
#         {"jokey":"George Orwell"},
#         {"$set":{"jokey": "Yekta"}}
           
            
    
# )






# çokluda:




x= {"jokey":"Yekta"}

y={"$set":{"fiyat": 100, "stok": 100}}

z= mycollection.update_many(x,y)
    
        
    
        
           
            
    




    
# for i in mycollection.find():
#     print(i)
# print(f"{mycollection.modified_count()} güncellendi")
# """


# update'de tırnaklara dikkat et bir atama yapmadan find donguye sok
# """


print(f"{z.modified_count}")
for i in mycollection.find():
    print(i)
