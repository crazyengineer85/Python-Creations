import pymongo
from bson.objectid import ObjectId
from pymongo.collation import Collation



myclient = pymongo.MongoClient("mongodb+srv://yektaduran_db_user:Test40123@cluster0.4mxlcx3.mongodb.net/")


mydb = myclient["kitabevi"]






mycollection = mydb["kitaplar"]










mycollection.create_index("yazar") # performans için sorgudan önce birkez yaz
# x = mycollection.find().sort("yazar",1).collation(Collation(locale="tr")) # türkçe karekter içeriyor
x = mycollection.find().sort([("yazar",-1),("fiyat",-1)])


    
for i in x:
    print(i)




"""

from pymongo.collation import Collation
mycollection.create_index("yazar") # performans için sorgudan önce birkez yaz
x = mycollection.find().sort("yazar",1).collation(Collation(locale="tr")) # türkçe karekter içeriyor
"""