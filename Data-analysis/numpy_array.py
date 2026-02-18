import numpy as np
import random


# x = np.arange(1,10)
# x = np.arange(1,10,2)
# x = np.zeros(10)
# x = np.ones(10)
# x = np.linspace(0,102,4)
# x = np.linspace(0,5,5)
# x = np.random.randint(0,10)
matris = []
for i in range(6):
    satir = []
    for j in range(6):
        satir.append(np.random.randint(1,50))
    matris.append(satir)
print(np.array(matris))



sayilar = random.sample(range(1,50),36)
list = []
index = 0

for i in range(6):
    row = []
    for j in range(6):
        row.append(sayilar[index])
        index+=1
    list.append(row)
print(f"\n************************TEKRARSIZ***************************")    
print(f"\n{np.array(list)}")


# print(type(x))