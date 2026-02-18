import mysql.connector



def insert_cok(list):
    mydb= mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "12345",
    database = "otomobiller"
    )






    mycursor = mydb.cursor()
    sql = "INSERT INTO araclar (name, marka, model, vites, yakit, fiyat) VALUES(%s,%s,%s,%s,%s,%s)"
    values = list


    mycursor.executemany(sql,values)

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
    if r== 1:
        x = input("name: ")
        y = input("marka: ")
        z = input("model: ")
        w = input("vites: ")
        q = input("yakıt: ")
        s = int(input("fiyatı: "))
        list.append((x,y,z,w,q,s))
          
    else:
        print("bilgiler yazılıyor.....")
        print(list)
        insert_cok(list)
        break
         
         