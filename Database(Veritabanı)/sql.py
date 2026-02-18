import sqlite3



mydb = sqlite3.connect("chinook.db") # Mysqlden farkı

mycursor = mydb.cursor()
mycursor.execute("Select * from customers")
x= mycursor.fetchall()
for i in x:
    print(i)

mydb.close()



