import pandas as pd
df = pd.read_csv("imdb.csv")


# 1- Dosya hakkında bilgiler:
# print (df)
# 2- ilk 5 kayıt
# print (df.head())
# 3- ilk 5 kayıt
# print (df.head(10))




# # 4- Son 5 kayıt
# print (df.tail())
# # 5- Son 10 kayıt
# print (df.tail(10))

# 6- sadece Movie_title

# df = df["Movie_Title"]
# print(df)
# 7- sadece Movie_title'ın ilk 5
# df = df["Movie_Title"].head()
# print(df)
# # 8- sadece Movie_title Rating ilk 5
# df = df[["Movie_Title","Rating"]].head()
# print(df)
# 9- sadece Movie_title Rating son 7

# df = df[["Movie_Title","Rating"]].tail(7)
# print(df)
# 10- sadece Movie_title Rating ikinci 5
# df = df[6:11][["Movie_Title","Rating"]].head() # *****belirlenecek index [6:11] dataframe'in başında yazılması lazım 
# print(df)


# 11-sadece Movie_title Rating ve imdb puanı 8.0 üstünde ilk 50
# print(df)

# df = df[df["Rating"] > 8.0][["Movie_Title","Rating"]].head(50)

print(df)
# 12- yayın tarihi 2014-2015 film isimleri

# df = df[(df["YR_Released"] >= 2014) & (df["YR_Released"] <= 2015)][["Movie_Title", "YR_Released"]]
# 2. Yol df = df.query("(YR_Released >= 2014) & (YR_Released <= 2015)")[["Movie_Title", "YR_Released"]]
# 3. Yol df = df.query("YR_Released.between(2014, 2015)")[["Movie_Title", "YR_Released"]]
# print(df)


# 13- Num_Reviews = 100000 den büyük, Rating =  8 - 9 arası film
#df = df.query("(Num_Reviews > 100000) & (Rating.between(8,9))")[["Movie_Title", "Rating", "Num_Reviews"]]
# df = df[(df["Num_Reviews"]> 100000) & (df["Rating"]>=8) & (df["Rating"]<=9)][["Movie_Title", "Rating", "Num_Reviews"]]
# df = df.query("Num_Reviews > 100000 &  Rating>=8 & Rating<=9")[["Movie_Title", "Rating", "Num_Reviews"]]
print(df)