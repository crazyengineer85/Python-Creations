# import json
# print(json.__file__) # bize json'ın path'ini verir


# request: internet sitelerinin kaynak dosyalarına erişmek için kullanılır..... json olarak verir


import requests as yekta
import json as j

x = yekta.get("https://jsonplaceholder.typicode.com/todos")
print(x)
# x = x.text # json formatında
x = j.loads(x.text) # jsonu dict-list formatına çevirdi

"""print(x)
print(type(x))
print(x[0]["title"])
print(x[0])"""

for i in x:
    print(i)
for i in x:
    if i["completed"]== True:
        print(i["title"])