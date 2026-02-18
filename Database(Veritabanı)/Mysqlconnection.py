# import mysql.connector 



# mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "12345" 
# )
# # print(mydb)




# mycursor = mydb.cursor()


# mycursor.execute("SHOW DATABASES")
# # mycursor.execute("CREATE DATABASE bahce")
# for i in mycursor:
#     print(i)













# mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "12345",
#     database = "bahce" 
# )
# # print(mydb)




# mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), adres VARCHAR(255))")










# import mysql.connector

# mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "12345"
# )

# mycursor = mydb.cursor()
# mycursor.execute("SHOW DATABASES")
# # mycursor.execute("CREATE DATABASE hollywood")
# for i in mycursor:
#     print(i)
# # print(mydb)


















# import mysql.connector




# mydb = mysql.connector.connect(
# host = "localhost",
# user = "root",
# password = "12345"

# )




# mycursor = mydb.cursor()
# # mycursor.execute("CREATE DATABASE  ezogelin")
# mycursor.execute("SHOW DATABASES")
# for i in mycursor:
#     print(i)
# # print(mydb)












































# import mysql.connector


# mydb = mysql.connector.connect(

# host="localhost",
# user="root",
# password="12345"

# )

# print(mydb)

# mycursor = mydb.cursor()
# # mycursor.execute("CREATE DATABASE bilgisayar_muhendisligi")








# mycursor.execute("SHOW DATABASES")
# for i in mycursor:
#     print(i)




import mysql.connector


mydb = mysql.connector.connect(

host="localhost",
user="root",
password="12345",
database="ezogelin"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE oyuncular (isim VARCHAR(15), age INT, Medeni_Durum BOOLEAN, odul_adi TEXT)")