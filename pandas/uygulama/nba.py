import pandas as pd
import numpy as np


# 1. cevap: ilk on kayıt

df =pd.read_csv("nba.csv")

# print(df.head(10))



# 2. cevap: toıplam kayıt sayısı

# df = len(df.index) # 458
# print(df)

# 3. cevap: Maaşların toplamının ortalaması

# df = df["Salary"].mean() # 4842684.105381166
# print(df) 

# 4. cevap: en yüksek maaş

# df = df["Salary"].max()

# print(df)


# # 5. cevap: en yüksek maaş kişi
# x = df["Salary"].max()
# df = df[df["Salary"]==df["Salary"].max()]["Name"].iloc[0] # burada 0. indexte veriyi yaz
# print(f" en yüksek maaş: {df} , para: {x}")

# 6. cevap: yas 20-25 oyuncu isim takım bunu büyükten küçü

# df = df[(df["Age"]>=20)&(df["Age"]<=25)][["Age","Name","Team"]].sort_values("Age",ascending = False)
# print(df)



# df = df[(df["Name"] ==  "John Wall")&(df["Age"]==25)][["Team","Name","Age"]]
# print(df)

# x = df.groupby("Team").mean(numeric_only=True)[["Salary","Age", "Weight"]]
# print(x)
# print(df.dtypes)



























# df = df.groupby("College").mean(numeric_only=True)["Salary"]
# print(df)

# df = df["Team"].unique()
# df = df["Team"].nunique()
# df = len(df.groupby("Team"))
# print(df)



# df = df.groupby("Team").count()["Name"]
# df = df["Team"].value_counts()
# print(df)
df.dropna(inplace=True) # nan gelen satırları yazdırmıyor
df = df[df["Name"].str.contains("and")]
print(df)