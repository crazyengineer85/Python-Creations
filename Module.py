# programı ayırdığımız parçadır (kütüphane)
# moduller arası kullanım vardır

# türleri:
# 1- kendi yazdığımız
# 2- hazır aldığımız
#   a- standart kütüphane = python geliştiricileri tarafından yazılır: math kütüphane
#   b- üçüncü şahıs = pypi.org
#       pip install package-name





# Yöntem 2
# import math as islem
# import math


# value = dir(math)
# value = help(math.factorial)





# value = math.sqrt(49)
# value = math.factorial(5)
# value = math.floor(5.9)
# value = math.ceil(5.9)
# value = islem.sqrt(49)
# value = islem.factorial(5)
# value = islem.floor(5.9)
# value = islem.ceil(5.9)
# print(value)


# def sqrt(x):
#     print('x: '+ str(x))

# from math import factorial,sqrt,ceil

# # def sqrt(x):
# #     print('x: '+ str(x))
# # value = factorial(5)
# value = sqrt(49)
# # value = ceil(9.9)
# print(value)
"""

Burada sqrt fonksiyonunu import'un üstüne alırsak sqrt methodunu yapar, iç tarafa yazarsak fonksiyonu yapıp 49 yazar




"""


import random


# x = dir (random)
# x = help(random)
x = random.random() # 0.0 ile 1.0 arasında bir sayı üretir
x = x*100
x = random.uniform(0,10)# 0 ile 10 arasında float              
x = int(random.uniform(0,10))
x = random.randint(10,100)



greeting = "hello yekta"
y = ['a', 'b', 'c', 'd']
# x = y[random.randint(0,len(y)-1)]
# x = random.choice(y) # bu diziler için yukardakine method olarak kullanılır
# x= random.choice(greeting)

# liste = list(range(10))
# x = liste
# random.shuffle(liste)
# x = liste

liste = list(range(100))
x = random.sample(liste, 3) # liste içerisinden kaç tane sample alarak
x = random.sample(y, 2)
print(x)




