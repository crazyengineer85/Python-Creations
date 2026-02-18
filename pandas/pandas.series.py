import pandas as pd
import numpy as np


# numbers = [1,2,3,4,5]
# letters = ['a','b','c','d','e']
# pandas_series = pd.Series() # Series([], dtype: object)
# pandas_series = pd.Series(numbers)
"""
0    1
1    2
2    3
3    4
4    5
dtype: int64


"""
# pandas_series = pd.Series(letters)
"""

0    a
1    b
2    c
3    d
4    e
dtype: str
"""
# letters = ['a','b','c','d',200]
# pandas_series = pd.Series(letters)




"""

0      a
1      b
2      c
3      d
4    200
dtype: object
"""
# scalar = 5
# pandas_series = pd.Series(scalar) 
"""

0    5
dtype: int64
"""
# pandas_series = pd.Series(scalar,[0,1,2,3])


"""
0    5
1    5
2    5
3    5
dtype: int64
"""

# numbers = [1,2,3,4]
# pandas_series = pd.Series(numbers,['a','b','c','d']) # burada sayı kadar yandaki liste
# dict = {'a':10,'b':20,'c':30,'d':40}
# pandas_series = pd.Series(dict)

"""
a    10
b    20
c    30
d    40
dtype: int64
"""

# random_numbers = np.random.randint(10,100,6)
# pandas_series = pd.Series(random_numbers)

pandas_series = pd.Series([10,20,30,40],['a','b','c','d'])
# x = pandas_series['a']
# x = pandas_series[['a','b']]
# x = pandas_series.ndim
# x = pandas_series.shape
# x = pandas_series.sum()
# x = pandas_series.max()
#x = pandas_series + pandas_series
# x = pandas_series +50
# x = np.sqrt(pandas_series)
# x = pandas_series > 50
# x = pandas_series % 2 == 0
# print(pandas_series[x])
"""
opel2018 = pd.Series([10,20,30,40],['astra','corsa','Mokka','Insignia'])
opel2019 = pd.Series([40,30,20,10],['astra','corsa','Grandland','Insignia'])
total = opel2018 + opel2019
print(total['astra'])
print(total)"""


# pandas_series = pd.Series([1,2,3,4],['a','b','c','d'])
# x = pandas_series.iloc[0]
# print(pandas_series)
# print(x)

pandas_series = pd.Series([1,2,3,4],['a','b','c','d'])
x = pandas_series.iloc[0]
print(pandas_series)
print(x)
