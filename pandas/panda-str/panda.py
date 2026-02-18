# import pandas as pd



# data = pd.read_csv("nba.csv")

# data.dropna(inplace=True) # burada "nan" gelen kayıtları düzen kopyasını alma değişken atayıp orjinal dosyayla çalış
# print(data.columns)
# # data["Name"] = data["Name"].str.upper()
# # data["Name"] = data["Name"].str.lower()
# data["index"] = data["Name"].str.find("a") # burada index ile harf arama geri döndürülen en son index


# data = data.Name.str.contains("Jordan") # buradan true false olarak gelir
# data = data[data.Name.str.contains("Jordan")] # burayı dataframe'e çevirerek yazıldığında veri gelir
# print(data.head(10))























import pandas as pd



data = pd.read_csv("nba.csv")

data.dropna(inplace=True)
# print(data)
# data = data[data["Team"].str.contains("Los")]
# data = data[data["Team"].str.contains("Lakers")]
# data["index"] = data.College.str.contains("Kentucky")
# data = data[data["College"].str.contains("Kentucky")] # College = kentucky
# data =data.Team.str.replace(' ','-')
#data[["First name","Last name"]] = (data["Name"].loc[data["Name"].str.split().str.len()==2].str.split(expand=True))
# data[["First name", "Last name"]] = data["Name"].str.split(n=1, expand=True)
# print(data)



# data[["First name","Last name"]] = (data["Name"].loc[data["Name"].str.split().str.len()==2].str.split(expand=True))
data["A","B"] = (data["Name"].loc[data["Name"].str.split().str.len()==2].str.split(expand=True))
print(data.head(10))