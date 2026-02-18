def greeting(name):
    print("hello"+ " "+name)





# greeting("Yekta")
# print(greeting)





sayhello = greeting



# print(sayhello)# adresleri ayni <function greeting at 0x0000027CF59A1440>
# print(greeting)# adresleri ayni <function greeting at 0x0000027CF59A1440>



# print(greeting("Yekta"))
# print(sayhello("Yekta"))


# del sayhello
# print(sayhello) # sayhelloyu sildiğin için NameError: name 'sayhello' is not defined hatasını verir
# print(greeting) # ilgili adresteki data çalış



#encapsulation 
# def outer(num1):
#     print('outer')
#     def innerincreament(num1):
#         print('inner')
#         return num1+1
#     num2 = innerincreament(num1) # içtekıi fonksiyonu çağırma
#     print(num1,num2)
# outer(10)
# innerincreament(10) # NameError: name 'innerincreament' is not defined






# def factorial(num):
#     if not isinstance(num, int):
#         raise Exception ("number must be integer")
#     elif not num>=0:
#         raise Exception ("number must be zero or positive")

#     def inner_factorial(num):
#         if num<1:
#             return 1
#         return num*inner_factorial(num-1)
#     return inner_factorial(num)
# try:
#     x = int(input("gir: "))
#     print(factorial(x))
# except Exception as e:
#     print (f"düzgün gir {x}: ", e)




def factorial(x):
    def innerfactorial(x1):
         if x1<1:
             return 1
         return x1* innerfactorial(x1-1)
    return innerfactorial(x)

print(factorial(3))









