# import pandas as pd



personel = {

"Çalışan": ["Ahmet Yılmaz","Can Ertürk","Hasan Korkmaz","Cenk Saymaz", "Ali Turan", "Rıza Ertürk", "Mustafa Can"],
"Departman": ["İnsan Kaynakları", "Bilgi İşlem", "Muhasebe", "İnsan Kaynakları", "Bilgi İşlem", "Muhasebe", "Bilgi İşlem"],
"Yaş": [30,25,45,50,23,34,42],
"Semt": ["Kadıköy", "Tuzla", "Maltepe", "Tuzla", "Kadıköy", "Tuzla", "Maltepe"],
"Maaş": [5000, 3000, 4000, 3500, 2750, 6500, 4500]

}
# for key, value in personel.items():
#     # print(key)
#     print(value)
# dataframe_cevir = pd.DataFrame(personel)
# print(dataframe_cevir)
# toplam_maas = dataframe_cevir["Maaş"].sum()
# print(f"\n\n Çalışanların maaş toplamı: {toplam_maas}")



# yas_ortalaması = dataframe_cevir["Yaş"].mean()

# print(f"\n\n Çalışanların yaş otalaması: {yas_ortalaması}")

# x = dataframe_cevir.groupby("Departman").groups

# print(x)
# y = dataframe_cevir.groupby("Semt").groups
# print(y)




# w = dataframe_cevir.groupby(["Departman", "Semt"]).groups
# print(w)

# 1. yol
# semt = dataframe_cevir.groupby("Semt")
# # print(semt)
# print("\n\n")
# for key, deger in semt:
#     print(key)
#     print(deger)

# 2. Yol
# print("\n\n")
# for key, deger in dataframe_cevir.groupby("Semt"):
#     print(key)
#     print(deger)


# print("\n\n")
# for key, deger in dataframe_cevir.groupby("Departman"):
#     print(key)
#     print(deger)

# departman = dataframe_cevir.groupby("Departman").get_group("Bilgi İşlem")

# print(departman)


















import pandas as pd
import numpy as np


personel = {

"Çalışan": ["Ahmet Yılmaz", "Can Ertürk", "Hasan Korkmaz", "Cenk Saymaz", "Ali Turan","Rıza Ertürk", "Mustafa Can"],
"Departman": ["İnsan Kaynakları", "Bilgi İşlem", "Muhasebe", "İnsan Kaynakları", "Bilgi İşlem", "Muhasebe", "Bilgi İşlem"],
"Yaş": [30,25,45,50,23,34,42],
"Semt": ["Kadıköy", "Tuzla", "Maltepe", "Tuzla", "Kadıköy", "Tuzla", "Maltepe"],
"Maaş": [5000, 3000, 4000, 3500, 2750, 6500, 4500]
    
}
df = pd.DataFrame(personel)
# Departman = df.groupby("Departman").groups
# Insan_Kaynakları = df.groupby("Departman").get_group("İnsan Kaynakları")
# print(Insan_Kaynakları)
# Insan_Kaynakları = df.groupby("Departman")["Maaş"].max()["İnsan Kaynakları"]
# print(Insan_Kaynakları)
# dep = df.groupby("Departman").mean(numeric_only=True)
# dep = df.groupby("Departman")[["Yaş", "Maaş"]].agg(np.mean)
# 1. Yol
#  dep = df.groupby("Departman")["Maaş"].agg([np.sum, np.mean, np.max, np.min])
# 2. Yol
#  dep = df.groupby("Departman")["Maaş"].agg(toplam_maaş = "sum", ortalama_maaş="mean", max_maaş="max", min_maaş="min")
# 3. Yol
# dep = df.groupby("Departman")["Maaş"].agg([np.sum, np.mean, np.max, np.min])
# dep.columns =["toplam_maaş", "ortalama_maaş", "max_maaş", "min_maaş"]
# dep = df.groupby("Departman")["Maaş"].agg([np.sum, np.mean, np.max, np.min]).loc["Bilgi İşlem"] # burda yana yazılıyor
print(dep)




