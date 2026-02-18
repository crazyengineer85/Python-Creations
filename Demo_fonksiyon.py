# def yaz(kelime, adet):
#     print(kelime*adet)
# yaz ('Yekta\n',8)

# def list(*params):
#     list = []
#     for i in params:
#         list.append(i)
        
#     return list
# x = list(1,2,3,4,5,6,7,8,9)
# print(x)







# def asalbul(say1, say2):
#     for i in range(say1,say2+1):
#         if i> 1:
#             for j in range (2, i):
#                 if i%j==0:
#                     break
#             else:
#                 print(i)


# say1 = int(input("say1: "))
# say2 = int(input("say2: "))
# asalbul(say1, say2)







def tambolen(say):
    list = []

    for i in range(2,say):
        if say%i==0:
            list.append(i)
    return list
print(tambolen(60))


