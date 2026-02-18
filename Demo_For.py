sayilar = [1, 3, 5, 7, 9, 12, 19, 21]
# 1- 

# for x in sayilar:
#     if x%3==0:
#         print(x)

# 2-

sayilar = [1, 3, 5, 7, 9, 12, 19, 21]
# topla=0
# for x in sayilar: 
#     topla = topla + x
# print(topla)





# for x in sayilar:
#     if x%2!=0:
#         print(f"{x}. karesi: {x**2}")


sehirler = ['kocaeli', 'istanbul', 'ankara', 'izmir', 'rize']
# for x in sehirler:
#     if len(x)<=5:
#         print(x)


# 3-
urunler =[{'name':'samsung S6', 'price': '3000'},
          {'name':'samsung S7', 'price': '4000'},
          {'name':'samsung S8', 'price': '5000'},
          {'name':'samsung S9', 'price': '6000'},
          {'name':'samsung S10', 'price': '7000'}
          ]
# topla= 0
# for x in urunler:
#     # print(x['price'])
#     topla = topla + int(x['price'])
# print(topla)





for x in urunler:
    if int(x['price'])<=5000:
        print(x['name'])