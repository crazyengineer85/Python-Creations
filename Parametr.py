# def change(g):
#     g[0]='Istanbul'

# sehir = ['ankara', 'izmir'] # Value typelarda değişmez referans typelarda değişir değişkene bakmaz
# change(sehir)

# print(sehir)












# sehir dizisinin bir kopyası slicing
# 1. Yol:
# def change(g):
#     g[0]='Istanbul'

# sehir = ['ankara', 'izmir']
# g[0] = 'Istanbul'

# print(sehir)

# 2. Yol:
# def change(g):
#     g[0]='Istanbul'

# sehir = ['ankara', 'izmir']
# change(sehir[:])

# print(sehir)


# def add(a, b):
#     return sum((a,b))
# print(add(60,10))
# def add(*params):
#     return sum((params))
# print(add(60,10,20))




# def add(*params):
#     sum = 0
#     for g in params:
#         sum = sum + g
#     return sum
# print(add(60,10,20))




# def displayuser(**args):
#     print(type(args))
#     for key, value in args.items():
#         print('{} is {}'.format(key,value))
# displayuser(name ='Yekta', age = 40, city = 'Istanbul' )
# displayuser(name ='Barış', age = 32, city = 'Belçika' )




def myfun(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
myfun(10,20,30,40,50,60,70,key1 ='value1', key2= 'value2')