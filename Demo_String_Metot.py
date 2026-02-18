website = "http://www.yektaduran.com"
course  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)" 

# 1- ' Hello World ' dizisinin baş ve sondaki boşluk karakterlerini kal
# x = ' Hello World '
# x = x.strip()
#x = x.lstrip()#soldaki boşluğu sil
# x = x.rstrip()#sağdaki boşluğu sil

# x = "http://www.yektaduran.com".lstrip('/:pth')
# 2- "yektaduran" içindeki 'a,d' sil


# x = "yektaduran".split('d')
# y = x[0].rstrip('a')
# # print(x)
# # print(y)
# x = y + ' ' +x[1]
# print(x)
# 3- "www.yektaduran.com" yektaduran kalacak

# x = "www.yektaduran.com".strip('w,.,c,o,m')
# print(x)
# 4- course'un hepsi küçük
# print(course)
# x = course.lower()
# print(x)
# 5- website ta kaç a var? (count(a))
# x = website.count('a')
# print(x)
# 6- course içinde kaç 'a' var=

# x= course.count('a'),course.count('o')
# print(x)
# 7- website da www ile başlayıp com ile bitiyor mu?
# x = website.startswith('www')+website.endswith('com')
# print(x)
# 8- 'contents' ifadesinin 50 karekter yerleştirip sağ ve soluna yıldız koy
# x = 'content'
# # 1.yol
# # sonuc = ''
# # for i in x:
# #     sonuc += i+ '  '
# # sonuc = sonuc.strip()      
# # # print(sonuc)
# # 2. Yol
# # sonuc = '  '.join(x)
# sonuc = sonuc.center(50,'-')
# print(sonuc)
# 10- course dizisini boşluk yerine - koy
# x = course.replace(' ','**')
# print(x)
# 11- "Hello World" "Bu Dünya" diye değiştir
# x = 'Hello World'.replace('Hello World', 'Kahpe Dünya')
# print(x)
# 12- Course karakter dizisindeki boşluk karakter dizisinden ayırın
x = course.split(' ')
print(x)
x = '*'.join(x)
print(x)