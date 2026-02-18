import numpy as np
import random
import math
# 1- (10,15,30,45,60) array oluşturma?
# np_array = np.array([10,15,30,45,60])
# print(np_array)



# 2- 5 ile 15 arasındaki sayılar?

# np_array = np.arange(5,15)
# print(np_array)



# 3- 5 ile 100 arasında 5'er 5'er?

# np_array = np.arange(5,100,5)
# print(np_array)

# 4- 10 tane 0. oluşturma?

# np_array = np.zeros(10)

# print(np_array)

# 5- 10 tane 1. oluşturma?

# np_array = np.ones(10)
# print(np_array)





# 6- 0 ile 100 arasında eşit aralıklı 5 sayı?

# np_array = np.linspace(0,100,5)
# print(np_array)


# 7- 10 ile 30 arasında rastgele 5 tam sayı?
# np_array = np.random.randint(10,30,5)
# print(np_array)

# np_array = np.random.choice(range(10,30),size=(1,5),replace=False)
# print(np_array)


# 8- [-1 ile 1] arasında 10 adet sayı?


# np_array = np.random.uniform(-1,1,10)
# print(np_array)





# 9- 3x5 boyutlarında (10,50) arasında rastgele matris?

# np_array = np.random.choice(range(10,50),size=(3,5))
# print(np_array)
# np_array = np.random.randint(10,50,15)
# print(np_array.reshape(3,5))

#10- 3x5 boyutlarında (10,50) arasında rastgele matris satır sütun toplamı
# np_array = np.random.randint(10,50,15).reshape(3,5)
# print(np_array)
# satir = np_array.sum(axis=1)
# sutun = np_array.sum(axis=0)


# print(f"\n\nsatır toplamı: {satir}, sütun toplamı: {sutun}")

#11- 3x5 boyutlarında (10,50) arasında rastgele matris en büyük, en küçük ve ortalaması?

# np_array = np.random.randint(10,50,15).reshape(3,5)
# print(np_array)
# min = np_array.min()
# max = np_array.max()
# avg = np_array.mean()
# print(f"\n\n min: {min}, max:{max}, ortalama:{avg}")
# 12- 3x5 boyutlarında (10,50) arasında rastgele matris en büyük index, en küçük index ?
# np_array = np.random.randint(10,50,15).reshape(3,5)
# print(np_array)
# min_index = np_array.argmin()
# max_index = np_array.argmax()
# print(f"\n\n min index: {min_index}, max index:{max_index}")



# 13- (10,20) arasında dizinin ilk 3 ?
# np_array = np.arange(10,20)
# print(np_array)
# x = np_array[0:3]
# print(x)


# 14- (10,20) dizinin tersten ?
# np_array = np.arange(10,20)
# print(np_array)
# x = np_array[::-1]
# print(x)
# x = np_array[:-4:-1]
# print(x)

# 15- 3x5 boyutlarında (10,50) arasında rastgele matris ilk satır seç ?
# np_array = np.random.randint(10,50,15).reshape(3,5)
# print(np_array)
# print("\n\n")
# print(f"ilk satır: {np_array[0]}")
# print(f"iki satır: {np_array[1]}")
# print(f"uc satır: {np_array[2]}")

# 16- 3x5 boyutlarında (10,50) arasında rastgele matris iki satır uc sutun ?
# np_array = np.random.randint(10,50,15).reshape(3,5)
# print(np_array)
# print("\n\n")
# print(f"ikinci satır ucun sutun: {np_array[1][2]}")




# 17- 3x5 boyutlarında (10,50) arasında rastgele matris tüm satırlarındaki ilk eleman ?
# np_array = np.random.randint(10,50,15).reshape(3,5)
# print(np_array)
# print("\n\n")
# print(f"tüm satırlarındaki ilk eleman: {np_array[:,0]}")

# 18- 3x5 boyutlarında (10,50) arasında rastgele matris her elemanın karesi ?
# np_array = np.random.randint(10,50,15).reshape(3,5)
# print(np_array)
# print("\n\n")
# print(np_array**2)


# 19- 3x5 boyutlarında (-50,+50) arasında rastgele matris hangisi pozitif hangisi negatif çift sayı?
np_array = np.random.randint(-50,50,15).reshape(3,5)
print(np_array)
print("\n\n")

x = np_array[np_array%2==0]
print(x)
pozitif_cift = x[x>0]
negatif_cift = x[x<0]

 


print(f"\n\n pozitif_cift: {pozitif_cift}, \n\nnegatif_cift:{negatif_cift}")

