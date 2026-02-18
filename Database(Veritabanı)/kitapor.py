import pymongo



myclient = pymongo.MongoClient("mongodb+srv://yektaduran_db_user:Test40123@cluster0.4mxlcx3.mongodb.net/")


mydb = myclient["kitabevi"]

print(mydb.list_collection_names())




collection = mydb["kitaplar"]
# kitap_listesi = [
#     {
#         "kitap_adi": "1984",
#         "yazar": "George Orwell",
#         "fiyat": 90,
#         "stok": 30
#     },
#     {
#         "kitap_adi": "Ateşten gömlek",
#         "yazar": "Halide edip",
#         "fiyat": 100,
#         "stok": 50
#     },
#     {
#         "kitap_adi": "Çalıkuşu",
#         "yazar": "Reşat nuri",
#         "fiyat": 150,
#         "stok": 90
#     },
#     {
#         "kitap_adi": "Orient express cinayet",
#         "yazar": "agatha cristie",
#         "fiyat": 100,
#         "stok": 50
#     },
#     {
#         "kitap_adi": "İstiklal savaşı",
#         "yazar": "hulusi kentmen",
#         "fiyat": 175,
#         "stok": 100
#     }
# ]
# sonuc = collection.insert_many(kitap_listesi)
# print(f"eklenen id: {sonuc.inserted_ids}")
for i in collection.find():
    print(i)






