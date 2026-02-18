# # x = input('ad: ')
# # y = int(input('yaş: '))
# # z = input('eğitimi: ')

# # if ((y>=18)and((z=='Lise'or z=='lise')or(z=='Üniversite'or z=='üniversite'))):
# #     print(f"{x} isimli kişi ehliyet alabilir")
# # else:
# #     print(f"{x} isimli kişi ehliyet alamaz")

# # x = input('ad: ')
# # y = int(input('Doğum Tarihi: '))
# # z = input('eğitimi: ')

# # if (((2026-y)>=18)and((z=='Lise'or z=='lise')or(z=='Üniversite'or z=='üniversite'))):
# #     print(f"{x} isimli kişi {(2026-y)} yaşında ehliyet alabilir")
# # else:
# #     print(f"{x} isimli kişi {(2026-y)} yaşında ehliyet alamaz")

# # w = input('ad: ')
# # x = int(input('1.yaz: '))
# # y = int(input('2.yaz: '))
# # z = int(input('söz: '))

# # c = (x+y+z)/3
# # print(c)
# # if c>=0 and c<=24:
# #     print (f"{w} adlı kişi {c} notu alıp 0 aldı")
# # elif c>=25 and c<=44:
# #     print (f"{w} adlı kişi {c} notu alıp 1 aldı")
# # elif c>=45 and c<=54:
# #     print (f"{w} adlı kişi {c} notu alıp 2 aldı")
# # elif c>=55 and c<=69:
# #     print (f"{w} adlı kişi {c} notu alıp 3 aldı")
# # elif c>=70 and c<=84:
# #     print (f"{w} adlı kişi {c} notu alıp 4 aldı")
# # elif c>=85 and c<=100:
# #     print (f"{w} adlı kişi {c} notu alıp 5 aldı")


# # w = input('MARKA: ')
# # x = (input('SAhIP: '))
# # y = 2026 - int(input('Tescil tarihi: '))

# # # print(f"{x} sahipli {w} marka araç {y}. bakımını yapacaktır")
# # if y == 1:
# #     print(f"{x} sahipli {w} marka araç 1. bakımını yapacaktır")
# # elif y==2:
# #     print(f"{x} sahipli {w} marka araç 2. bakımını yapacaktır")
# # else:
# #     print(f"{x} sahipli {w} marka araç {y}. bakımını yapacaktır")




# import datetime

# # c = datetime.datetime.now() #yıl/ay/gün
# # print(c)

# x = input('1. Doğum tarihi (yıl/ay/gün): ')
# # y = input('2. Doğum tarihi (yıl.ay.gün): ')
# x = x.split('/')
# # y = y.split('.')
# print(x)
# # print(y)
# age_yekta = datetime.datetime(int(x[0]),int(x[1]),int(x[2]))
# # age_baris = datetime.datetime(int(y[0]),int(y[1]),int(y[2]))
# c = datetime.datetime.now()
# yas_yekta = c - age_yekta
# print(yas_yekta)
# yas_yekta = yas_yekta.
# print(yas_yekta)
# # yas_baris = c - age_baris
# # print(yas_baris)
# # kardes = yas_yekta - yas_baris
# # print(kardes)
# # q = kardes.days
# # print(f"Yekta Danası Barış Sıpasından {q} gün büyüktür")
# # w = yas_yekta - yas_baris
# # print(f"Yekta Danası Barış Sıpasından {w} büyüktür")




