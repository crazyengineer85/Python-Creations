# def my_Decorator(fun):
#     def wrapper():
#         print("fonksiyondan once islem")
#         fun()
#         print("fonksiyondan sonra islem")
#     return wrapper
# # 1. Yol
# # # def hello():
# #     print("hello")
# # def greeting():
# #     print("greeting")




# # # hello = my_Decorator(hello)
# # greeting = my_Decorator(greeting)
# # hello()
# # greeting()
# @my_Decorator
# def hello():
#     print("hello")
# hello()
# @my_Decorator
# def greeting():
#     print("greeting")
# greeting()

import math
import time
def calculatetime(fun):

    def wrapper(*args, **kwargs):
        start = time.time()
        time.sleep(1)
        x =fun(*args,**kwargs)
        finish = time.time()
        print(f"fonksiyon baslangıç: {start}, bitis: {finish}, {fun.__name__} ,saniye surdu: {finish-start}")
    return wrapper    
    
@calculatetime

def usalma(a,b):
    print(math.pow(a,b))
@calculatetime
def factorial(num):
    print(math.factorial(num))
   
usalma(2,3)
factorial(4)