import mysql.connector





# mycursor.execute("CREATE DATABASE otomobiller")
# mycursor.execute("SHOW DATABASES")
# for i in mycursor:
#     print(i)
# mycursor.execute("CREATE TABLE araclar (name VARCHAR(45) NOT NULL, marka VARCHAR(45) NOT NULL, model VARCHAR(45) NOT NULL, vites VARCHAR(45) NOT NULL, yakit VARCHAR(45) NOT NULL, fiyat INT NOT NULL, Id INT PRIMARY KEY NOT NULL AUTO_INCREMENT)")




def insert(x, y, z, w, q, s): # teker
    mydb= mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "12345",
    database = "otomobiller"
    )





    # print(mydb)
    mycursor = mydb.cursor()
    sql = "INSERT INTO araclar (name, marka, model, vites, yakit, fiyat) VALUES(%s,%s,%s,%s,%s,%s)"
    values = (x, y, z, w, q, s)


    mycursor.execute(sql,values)

    try:
        mydb.commit()
        print(f"enson eklenen kayıt: {mycursor.rowcount}")
        print(f"en son eklenen kayıt id: {mycursor.lastrowid}")
    except mysql.connector.Error as err:
        print("hata: ",err)
    finally:
        mydb.close()
        print("db kapatıldı")
list = []
while True:
    r = int (input ("insert için 1'e çıkmak için 2 ye basın: "))
    if r==1:
            x = input("name: ")
            y = input("marka: ")
            z = input("model: ")
            w = input("vites: ")
            q = input("yakıt: ")
            s = int(input("fiyatı: "))
            # list.append((x,y,z,w,q,s))
            insert(x,y,z,w,q,s)
            
    else:
         print("bilgiler yazılıyor.....")
        #  print(list)
         
         break
         
    
         
    
    
    
    

# insert("yaris","toyota","cross","otomatik","benzin",2100000)


