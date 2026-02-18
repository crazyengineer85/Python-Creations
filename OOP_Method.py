# class Person2:

# # class attribute
#     address = "no information"






# # constructor (yapıcı metodlar)
#     def __init__(self, name, year):
#        # object attributes
#         self.name = name  
#         self.year = year
    
    
#     # Method
#     def intro(self): # Bu method class'a hizmet eder
#         print("Hello There "+ "I'am "+self.name)
#     def calculateAge(self):
#         return 2026-self.year
   




# # object
# p1 = Person2('Yekta', 1985)
# p2 = Person2('Barış', 1993)






# p1.intro() # class'a hizmet eden methodu () ile çağıracağız
# p2.intro()

# print(f"adım: {p1.name}, yaşım: {p1.calculateAge()}")
# print(f"adım: {p2.name}, yaşım: {p2.calculateAge()}")

"""
hata almamızdaki sebep buradaki methodun bir instance Method olması = yani oluşturduğumuz objelere hizmet edecek bir method
en az objenin bir referansını "self"le vereceksin
"""



class Circle:
    pi = 3.14
    def __init__(self, yaricap=1):
        self.x = yaricap
    def cevre_hesapla(self):
        return 2*self.pi*self.x
    def alan_hesap(self):
        return self.pi*(self.x**2)

c1 = Circle()
print (f"cevre: {c1.cevre_hesapla()}, alan: {c1.alan_hesap()}")
c2 = Circle(9)
print (f"cevre: {c2.cevre_hesapla()}, alan: {c2.alan_hesap()}")