website = "http://www.yektaduran.com"
course  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)" 

# 1- 'course' karakter dizisinde kaç karakter var?
# x = len(course)
# print(x)
# 2- 'website' içinden www karekterini al
# x = website[7:10]
# print(x)
# 3- 'website' içinden com karekterini al
# x = website[-3:]
# print(x)
# 4- 'course' içinden ilk 15 ve son 15 karakterlerini al
# x = course[:15] +' '+ course[-15:]
# print(x)
# 5- 'course' ifadesini tersten yazdır
# x = course[:]
# w = course[::-1]
# #print(x)
# print(w)

# name, surname, age, job = 'Yekta', 'Duran', 40, 'Mühendis'
# # 6- Yukarıda verilen değişkenler ile ekrana:
# # 'Benim adım Yekta Duran, yaşım 40 ve mesleğim Mühendis'
# #print(f"Benim adım {name} {surname}, yaşım {age} ve mesleğim {job}")
# print(f"Benim adım {name} {surname}, \nyaşım {age} ve \nmesleğim {job}")

# 7- 'Hello world' ifadesinde 'w' harfini 'W' ile değiştir
x = "Hello world"

# x = x[:6]+'W'+ x[7:]
# print(x)
# x = x.replace('w','W')
# print(x)

y = "Hello World"
# y = y.replace('W','w')
# print(y)

# y= y[:6]+ 'w' + y[7:]

# print(y)

# y = y[:6] + y[6:].upper()
# print(y)


# 8- 'abc' ifadesinde 3 kere yanyana yazdır
x = "abc"
# x = x*3
# print(x)
# x = (x+"\n")*3
# print(x)
# x = (x+" ")*3
# print(x)
x = (x+("\n"*4))*3
print(x)