import mysql.connector



def aggregate():
    mydb= mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "12345",
    database = "otomobiller"
    )






    mycursor = mydb.cursor()
    # mycursor.execute("SELECT COUNT(name) FROM araclar")
    # mycursor.execute("SELECT AVG(fiyat) FROM araclar")
    # mycursor.execute("SELECT SUM(fiyat) FROM araclar")
    # mycursor.execute("SELECT name, vites FROM araclar where fiyat = 1600000 and yakit = 'benzin'")
    mycursor.execute("SELECT marka, yakit, fiyat from araclar where name LIKE '%Pan%'")
    x = mycursor.fetchone()
    print(f"name: {x[0]}, yakıt: {x[1]}, fiyat: {x[2]}")
aggregate()





         
         