import mysql.connector



# def y():
#     mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="12345",
#     database="otomobiller"
#     )

#     mycursor=mydb.cursor(dictionary=True)
#     mycursor.execute("Select * from araclar inner join categories on categories.Id = araclar.categoryId where fiyat> 100000")
#     y = mycursor.fetchall()   
#     for i in y:
#         print(i)
#     mydb.close()
    
    
    
    
    
   
# y()














def y():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="ahenk"
    )

    mycursor=mydb.cursor(dictionary=True)
    mycursor.execute("Select * from urunler inner join categories on categories.CategoryId = urunler.CategoryId")
    y = mycursor.fetchall()   
    for i in y:
        print(i)
    mydb.close()

y()