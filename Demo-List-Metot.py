names = ['Ali','Yağmur','Hakan','Deniz']
years = [1998, 2000, 1998, 1987]

# # 1-
# names.append('Cenk')
# # names.insert(4, 'Cenk')
# # print(names)
# # 2-
# names.insert(0, 'SENA')
# print(names)
# 3-
# names = ['Ali','Yağmur','Hakan','Deniz']
# # names.pop()
# # names.remove('Deniz')
# names.remove('YAĞMUR')
# print(names)
# 4-
# print(names.index('Deniz'))
# 5-

# x = 'Ali' in names
# x = 'Barış' in names

# names.reverse()
# print(names)

# names.sort(reverse=True)
# print(names)
# years.sort(reverse=True)
# print(years)
# years.reverse()
# print(years)
# str = "Chevrolet, Renault".split()
# print(str)

# x = min(years) 
# y = max(years)
# print(x, y)
# years = [1998, 2000, 1998, 1987]
# x = years.count(1998)
# print(x)
x = []
for i in range(3):
    brand = input("araba Marka gir: ")
    x.append(brand)
    
print(x)
