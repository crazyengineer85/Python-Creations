import pandas as pd





# s1 = pd.Series([0,5,10,15])
# s2 = pd.Series([100,150,200,250])

# data = dict (apples=s1, pears=s2)
# data_to_dataframe = pd.DataFrame(data)
# print(data_to_dataframe)


# 2


dic_list = [

{"name": "Ali", "vize1": 40,"vize2": 70,"final": 80},

{"name": "Mehmet", "vize1": 30,"vize2": 30,"final": 30},

{"name": "kamil", "vize1": 40,"vize2": 50,"final": 60},

{"name": "yekta", "vize1": 80,"vize2": 70,"final": 80},

]

dataframe_cevir = pd.DataFrame(dic_list, index = [201,202,204,208] )
dataframe_cevir.index.name = "ogrenci_no"
dataframe_cevir = dataframe_cevir.rename(columns={"name":"ogrenci_adı"})

print(dataframe_cevir)
