import pymongo



# myclient = pymongo.MongoClient("mongodb://localhost:27017") # localde
myclient =pymongo.MongoClient("mongodb+srv://yektaduran_db_user:Test40123@cluster0.4mxlcx3.mongodb.net/")


mydb = myclient["kitabevi"]
# print(mydb) # sadece yarisciler yazdirir

# print(myclient.list_database_names()) # tüm listeyi yazdırır

print(f"collection: {mydb.list_collection_names()}")