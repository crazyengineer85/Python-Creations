import pandas as pd



x = pd.Series(["kuş","leylek","Devekuşu","keklik"])
y = pd.Series(["kurt","tay","Deve","eşek"])

data = dict( iki_ayakli = x, Dort_ayakli = y)

dataframe_cevir = pd.DataFrame(data)
print(dataframe_cevir)