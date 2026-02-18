# 1- "BMW, Mercedes, OPeL, MAZDA"elemanlarına sahip lisate
# x = ["BMW","Mercedes","OPeL", "MAZDA"]
# print (x)
# # 2- kaç elemanlı
# print(len(x))
# 3- ilk ve son eleman
# x = ["BMW","Mercedes","OPeL", "MAZDA"]
# y = x[0]
# w = x[-1]
# print (f"Listenin ilk elemanı '{y}' son elemanı '{w}' dur")
# 4- Mazda yerine Toyota
x = ["BMW","Mercedes","OPeL", "MAZDA"]
# x[-1] = "TOYOTA"
# x[1] = "ReNAULT"
# print(x)

# 5- Mercedes listenin elemanı?
# isfound = x[1] in x # bir liste içinde bir şeyin aramasını yapmak ve boolean değer (True, False) değer döndürmek istiyorsak
# print(isfound)
# 6- Liste -2 index değeri
# print (x[-2])
# 7- Liste 3 eleman
# print(x[0:3])
# 8- Listenin son iki elemeanı toyota ve renault
# 1.yol
# x[-1] = "ReNAULT"
# x[-2] =  "TOYOTA"
# 2. Yol
# x[-2:] = "TOYOTA", "ReNAULT"
# print(x)
# 9- Audi nissan ekle
x = ["BMW","Mercedes","OPeL", "MAZDA"]
# x = x + ["AUDI","nissan qasqai"]
# print(x)
# # 10- son elemanı sil
# # 1. yol
# # x.pop()
# # 2. yol
# del x[-1]
# print(x)
# tersten yazdırma
# print(x[::-1])

# Aşağıdaki verileri bir listede sakla

# studentA: A 2010, (70,60,70)
# studentB: B 1999, (80,80,70)
# studentC: C 1998, (80,70,90)

x = "studentA: A 2010, (70,60,70)".split()
y = "studentB: B 1999, (80,80,70)".split()
w = "studentC: C 1998, (80,70,90)".split()
students = x+y+w
students0 = [x]+[y]+[w]
# print(students)
# print(students0)
# print(students[0])
# print(students0[0])
# print(students[5])
# print(students0[5])
print(students[2])
print(students0[2])
