# # Class



# class Person:
#     pass

#     # attribute
#     # metod

# # object instance
# p1 = Person()# p1 objesi tanımladım
# print(p1) # Burada bize Person class'ından türemiş bir obje olduğunu ve bunun adresini vermektedir
# p2 = Person()
# print(p2) # p1 ve p2 objelerinin class'ı aynı adresi farklı
# print(type(p1))
# print(type(p2))# burdada p1, p2 class tipi aynı
# print(p1==p2)# class'lar aynı olmasına rağmen farklı obje

# attribute iki şekilde tanımlanır:
# 1- class seviyesinde - class attribute'lar
# 2- object seviyesinde - object attribute'lar


"""
1-  object attribute'lar constructor (yapıcı metodlar) içinde tanımlanır
2- def __init__(self): # burada self'in anlamı class'tan türetilen herhangi bir obje(instance)
3- yani obje üzerine bir değer atamak istiyorsam "self"i kullanacağım
3- "self"in üzerine hangi attribute'ları eklemek istiyorsam self'ten sonra parametre olarak belirleyeceğim (self,) diye yazacağım
4- burda tanımlanacak olan objeler üzerine ekleyecek olduğum attributelar (object attribute'lar) üzerine kullanıcının gönderdiği parametreleri aktaracağım
"""








class Person2:

# class attribute
    address = "no information"
# constructor (yapıcı metodlar)
    def __init__(self, name, year): # constructor denmesindeki neden buradaki __init__ method@u oluşturulan herbir obje içinn çalıştırılır
       # object attributes
        self.name = name  # = name kullanıcının gönderdiği name bilgisidir, = öncesindeki "name" başka bir isim değişkeni verebiliriz
        self.year = year  # = year kullanıcının gönderdiği year bilgisidir, = öncesindeki "year" başka bir isim değişkeni verebiliriz
        print("init methodu çalıştı")
   




# object
p1 = Person2('Yekta', 1985)
p2 = Person2('Barış', 1993)
print(p1) # adres
print(p2) # adres
# accessing object attributes 
print(f"name: {p1.name}, year: {p1.year}, adres: {p1.address}")
print(f"name: {p2.name}, year: {p2.year}, adres: {p2.address}")


# updating
p1.address = 'Canada'
p2.address = 'Belgium'


print(f"name: {p1.name}, year: {p1.year}, adres: {p1.address}")
print(f"name: {p2.name}, year: {p2.year}, adres: {p2.address}")



"""


 1- Burada her zaman kullanmayacağımız attribute'ler = class attribute'e yaz
 2- Obje ilk oluşturulduğunda tanımlanmasını, eklenmesini istediğimiz attribute'lar = object attribute'e yaz
"""