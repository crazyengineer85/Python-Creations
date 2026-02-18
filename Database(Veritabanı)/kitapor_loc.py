import pymongo



myclient = pymongo.MongoClient("mongodb://localhost:27017")


mydb = myclient["yarisciler"]

print(mydb.list_collection_names())




collection = mydb["taylar"]
# taylar_listesi = [
#     {
#         "tay_adi": "84",
#         "jokey": "George Orwell",
#         "fiyat": 90,
#         "stok": 30
#     },
#     {
#         "tay_adi": "19",
#         "jokey": "Ali",
#         "fiyat": 90,
#         "stok": 30
#     },
#     {
#         "tay_adi": "1978",
#         "jokey": "Yekta",
#         "fiyat": 90,
#         "stok": 30
#     },
    
# ]
# sonuc = collection.insert_many(taylar_listesi)
# print(f"eklenen id: {sonuc.inserted_ids}")
# # for i in collection.find(): # bütün göstermek
# for i in collection.find_one(): # ilk gelen satır
#     print(i)



for i in collection.find({},{"_id":0, "tay_adi":1, "jokey": 1 }): # _id yazımına dikkat (önce gelen "_")
    print(i)