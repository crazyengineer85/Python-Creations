import mysql.connector



# def update():
#     mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="12345",
#     database="otomobiller"
#     )

#     mycursor=mydb.cursor()
#     mycursor.execute("UPDATE araclar Set name='Landcruiser' where Id=6")
#     mydb.commit()
#     mycursor.execute("select * from araclar where Id=6")
    
#     y = mycursor.fetchone()
#     print(mycursor.rowcount, "kayıt update yapıldı")
#     print(f"update satırı:{y}")
#     mydb.close()
# update()






















# def update():
#     mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="12345",
#     database="otomobiller"
#     )

#     mycursor=mydb.cursor()
#     mycursor.execute("UPDATE araclar Set model='joy' where Id=4")
#     mydb.commit() #update - zorunlu
#     mycursor.execute("select * from araclar where Id=4")
    
#     y = mycursor.fetchone()   # update olan satır getir
#     print(mycursor.rowcount, "kayıt update yapıldı") # mycursor.rowcount = > kaç satır update miktar
#     print(f"update satırı:{y}")
#     mydb.close()
# update()















# def Delete():
#     mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="12345",
#     database="otomobiller"
#     )

#     mycursor=mydb.cursor()
#     mycursor.execute("Delete from araclar where Id=14")
#     mydb.commit() #update - zorunlu
#     y = mycursor.fetchone()   
#     print(f"Delete satırı:{y}")
    
    
    
#     print(mycursor.rowcount, "kayıt silindi") # mycursor.rowcount = > kaç satır Delete miktar
#     # mycursor.execute("select * from araclar")
#     # for i in mycursor:
#     #     print(i)
#     # mydb.close()
# Delete()
"""




mydb.commit()
👉 sadece UPDATE değil
✔ INSERT
✔ UPDATE
✔ DELETE
için gerekir.
"""



