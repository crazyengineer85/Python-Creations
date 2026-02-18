# x = int(input("sayı: "))

# y = x>=0 and x<=100
# if y:
#     print(f"{x} sayısı 0 100 arasında: {y}")
# else:
#     print(f"{x} sayısı 0 100 arasında: {y}")


# x = int(input("sayı: "))

# y = x>=0 and x%2==0
# if y:
#     print(f"{x} sayısı pozitif çift: {y}")
# else:
#     print(f"{x} sayısı pozitif çift: {y}")

# x = input("email: ")
# y = input("password: ")
# email = "yekta@gmail.com"
# passw = "12345"
# if x==email:
#     if y==passw:
#         print ("giriş yap")
#     else:
#         print("parola hatalı")
# elif x==email and y!=False:
#     print("email doğru parola hatalı")
# else:
#     print("ikisi de hatalı")


# x = int(input("sayı: "))
# y = int(input("sayı2: "))
# z = int(input("sayı3: "))

# if (x>0 and x>y and x>z):
#     print(f"{x} sayısı en büyük")
# elif (y>0 and y>x and y>z):
#     print(f"{y} sayısı en büyük")
# else:
#     print(f"{z} sayısı en büyük")

# w = input("ad: ")
# x = int(input("vize: "))
# y = int(input("vize2: "))
# z = int(input("final: "))
# ort = (((x+y)/2)*0.6)+(z*0.4)
# print(ort)





# if ort>=50 and z>=50:
#     print("{w} kişisi geçti")
# elif z>=70:
#     print("{w} kişisi geçti")
# else:
#     print("{w} kişisi kaldı")

w = input("ad: ")
x = float(input("boy(cm cinsinden yaz): "))
y = float(input("kilo: "))
z = round(y / ((x/100)**2))

if z>=0 and z<=18.4:
    print(f"{w} kişisi boy kitle endexi {z} statu: zayıf")
elif z>=18.5 and z<=24.9:
    print(f"{w} kişisi {z} statu: normal")
elif z>=25.0 and z<=29.9:
    print(f"{w} kişisi {z} statu: kilolu")
elif z>=30:
    print(f"{w} kişisi {z} statu: obez")