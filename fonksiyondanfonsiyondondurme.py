# def usalma(num):

#     def inner(power):

#         return num**power
#     return inner

# """

# Burada "return inner" yani fonksiyon döndürdük, buradaki fonksiyon two ve three isimlerine referans olarak atandı

# """
# two = usalma(2) # taban 2
# three = usalma(3) # taban 3
# print(two(3)) # 2 - 3. kuvveti
# print(three(4)) # 3 - 4. kuvveti



# def yetkisorgula(page):
#     def inner(rol):
#         if rol=="admin":
#             return f"{rol} rolunun {page} sayfasına ulasır"
#         else:
#             return f"{rol} rolunun {page} sayfasına ulasmaz"
#     return inner
# user1 = yetkisorgula("product edit")
# print(user1("admin"))

def islem(islemadi):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    def carpim(*args):
        carpim = 1
        for i in args:
            carpim*= i
        return carpim
    if islemadi == "toplama":
        return toplam
    elif islemadi == "carpma":
        return carpim
    
toplama = islem("toplama")
carpma = islem ("carpma")
print(toplama(1,2,3,4,5,6,7,8,9))
print(carpma(1,2,3,4,5,6,7,8,9))