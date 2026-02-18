import pandas as pd
import sqlite3


# df = pd.read_excel("il_ilce_listesi.xls")
# print(df)

connection = sqlite3.connect("flights.db")
df = pd.read_sql_query("select * from Observation",connection)
print(df)




connection = sqlite3.connect("titanic.db")
df = pd.read_sql_query("select * from Deck",connection)
print(df)