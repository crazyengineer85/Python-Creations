import pandas as pd
import numpy as np

# data = {
# "Column1": [1,2,3,4,5],
# "Column2": [10,20,15,20,25],
# "Column3": ["abcde","bcacc","adeaa","cbaff","deagg"]
# }

# df = pd.DataFrame(data) 




# # def kareal(x):
# #     return x*x

# # x = lambda x:x*x


# result = df
# result = df["Column2"].unique()
# listedeki elemanları yazar tekrar eden versa onlrı bir kez yazar
# result = df["Column2"].nunique()  # number of unique (tekrarsız eleman syısı) 
# result = df["Column2"].count()    # listedeki eleman sayısı
# result = df["Column2"].value_counts() # listedeki eleman sayılarından tekrar sayısı
# result = df["Column1"]*2          # butun elemanları ikiyle çarpar    
# result = df["Column2"].apply(kareal) # fonksiyonaa atama
# result = df["Column2"].apply(x)    # lambda atamaa yontemi
# result = df["Column2"].apply(lambda x:x*x) # lambda kullnama yontemi
# result = df["Column3"].apply(len)   # string elman sayısı
# result["Column4"] = df["Column3"].apply(len) # string elemansayısı ayrı columnda dikkat et!!!!! len string eleman sayısı!!!!!!!
# result = df.columns # indexler Index(['Column1', 'Column2', 'Column3', 'Column4'], dtype='str') kolon bilgisi
# result = len(df.columns) # column sayısı bilgisi
# result = df.index # index bilgisi RangeIndex(start=0, stop=5, step=1) 0 dan başlar 5 e kadar gider artış miktarı 1
# result = df.sort_values("Column2") # sıralama
# result = df.sort_values("Column3", ascending=False)


data = {
    "Ay": ["Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan"],
    "Kategori": ["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap","Giyim","Giyim","Giyim"],
    "Gelir": [20,30,15,14,32,42,12,36,52]
}
df = pd.DataFrame(data)
"""

        Ay    Kategori  Gelir
0    Mayıs  Elektronik     20
1  Haziran  Elektronik     30
2    Nisan  Elektronik     15
3    Mayıs       Kitap     14
4  Haziran       Kitap     32
5    Nisan       Kitap     42
6    Mayıs       Giyim     12
7  Haziran       Giyim     36
8    Nisan       Giyim     52


Burada Ktegori ve Ay kısmında tekrarlayan değerler var bunun için df.pivot_table() kullan
"""

df1 = df.pivot_table(index="Ay", columns="Kategori", values="Gelir")
print(df1)
"""


Kategori  Elektronik  Giyim  Kitap
Ay
Haziran         30.0   36.0   32.0
Mayıs           20.0   12.0   14.0
Nisan           15.0   52.0   42.0  Burada tekrar eden tgrupları sütun hale getiriyor
"""
df = df.pivot_table(index="Kategori", columns="Ay", values="Gelir")



"""

Ay          Haziran  Mayıs  Nisan
Kategori
Elektronik     30.0   20.0   15.0
Giyim          36.0   12.0   52.0
Kitap          32.0   14.0   42.0

"""

print(df)
# print(result)