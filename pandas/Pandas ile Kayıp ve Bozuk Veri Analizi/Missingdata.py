import pandas as pd
import numpy as np


data = np.random.randint(10,100,15).reshape(5,3)
df = pd.DataFrame(data, index= ["a","c","e","f","h"], columns=["Column1", "Column2", "Column3"])

df = df.reindex(index=["a","b","c","d","e","f","g","h"])

newcolumn = [np.nan,20,np.nan,40,np.nan,60,np.nan,80]




newindex = [np.nan,20,np.nan,40]



df["column4"] = newcolumn
df.loc["i"] = newindex
print(df)
# # df = df.drop('h', axis = 0)
# # df = df.drop(['c','e'], axis = 0)
# # df = df.drop("Column1", axis = 1)
# df = df.isnull()
# df = df.notnull()
df = df.notnull().sum()
print(f"\n\n {df}")
