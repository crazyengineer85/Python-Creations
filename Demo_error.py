# 1
# x = ['1','2','1a','2a','10','20','40c','50','80']

# for i in x:
#     try:
#         y = int(i)
#         print(y)
#     except Exception as e:
#         print(f"bu değer {i} tam sayıya çevrilmedi: ", e)
#         continue
#     # finally:
#     #     print("validation ok")


# 2
# # while True:
#     x = input("x: ")
#     if x=='q' or x=='Q':
#         break
            
#     try:
#         x = int (x)
#     except Exception as e:
#         print(f"bu değer {x} tam sayıya çevrilmedi: ", e)
#         continue
#     else:
#         print("nihayet sayı girebildin.....")








# def passcheck(psw):
#     turkcekarakter= "ıüöçşğİ"
    
#     for i in parola:
#         if i in turkcekarakter:
#             raise TypeError("türkçe karakter yok.....")
#         else:
#             pass
#     print("geçerli parola")


# parola = input("parola: ")
# try:
#     passcheck(parola)
# except Exception as e:
#     print(e)



# 4


def factorial(x):
    x = int(x)
    y= 1
    if x<0:
        y =1
    for i in range(1,x+1):
        y = y*i
    return y

for x in [5,10,20,30,-3,'10a']:
    try:
        y= factorial(x)
    except Exception as e:
        print (e)
        continue
    print(y)


    






