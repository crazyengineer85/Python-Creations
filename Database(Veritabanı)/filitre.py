import pymongo
from bson.objectid import ObjectId



myclient = pymongo.MongoClient("mongodb+srv://yektaduran_db_user:Test40123@cluster0.4mxlcx3.mongodb.net/")


mydb = myclient["kitabevi"]

# print(mydb.list_collection_names()) # bütün tablolar




mycollection = mydb["kitaplar"]

# sonuc = collection.insert_many(taylar_listesi)
# print(f"eklenen id: {sonuc.inserted_ids}")
# # for i in collection.find(): # bütün göstermek
# for i in collection.find_one(): # ilk gelen satır
#     print(i)



# for i in collection.find({"yazar":"Reşat nuri"},{"_id":0, "yazar":0, "fiyat":0}):
#     print(i)
# y = {"_id": ObjectId("6990dca9bd16a22985a03033")}
# x = mycollection.find_one(y,{"_id":0})
# print(x)

"""


Id ye göre sorgu yapmak için önce:
    1- from bson.objectid import ObjectId ekle
    2- y = {"_id": ObjectId("6990dca9bd16a22985a03033")}
       x = mycollection.find_one(y,{"_id":0})
       print(x) ekle


"""







# x = mycollection.find({
#     "yazar":{
#         "$in": ["Halide edip", "Reşat nuri"]
#     }
# })
x = mycollection.find({
    "yazar": {
        "$regex": "Halide|Reşat",
        "$options": "i"
    }
    
})
for i in x:
    print(i)
# print(mycollection.count_documents({})) # kaç kayıt geldiğini