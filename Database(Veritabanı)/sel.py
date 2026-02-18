import mysql.connector



def getir():
    mydb = mysql.connector.connect(
    host = "localhost",
    user= "root",
    password= "12345",
    database= "otomobiller"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM araclar")
    x = mycursor.fetchall()
    print(x)
    

getir()





















def getir_ezogelin():
    mydb = mysql.connector.connect(
        host = "localhost",
        user="root",
        password="12345",
        database="ezogelin"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM oyuncular")
    # mycursor.execute("SELECT isim, odul_adi from oyuncular")
    x = mycursor.fetchall() # bir tuple liste dondurur, for ile bütün satırlara ulaşırsın 
    # x = mycursor.fetchone() # ilk tuple kaydı getirir, bır kayıt for'a gerek yok
    # print(f"\n\n{x}")
    for i in x:
        print(f"isim: {i[0]}, odul: {i[3]}")
        
getir_ezogelin()


