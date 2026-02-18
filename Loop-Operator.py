# range
# for x in range(50,100,2):#burada başlangıç sayısı 50 dahil, 100'e kadar dahil değil, 2'şer atlama
#     print(x)
# print(list(range(50,100,2)))# Listeye çevirdik



# enumarate

greeting ='Hello'




# index = 0
# for x in greeting:
#     print(f'index: {index} Letter: {x}')
#     index+=1

# for index, x in enumerate(greeting):
#     print(f'index: {index} Letter: {x}')

# for item in enumerate(greeting): # bize index ve karşılık gelen elemanı tuple olarak verir
#     print(item)
# print(type(item))


# zip




x = [1, 2, 3, 4, 5]
y = ['a', 'b', 'c', 'd', 'e']



print(list(zip(x,y)))

for item in zip (x, y):
    print(item)
print(type(item))

for x,y in zip (x, y):
    print(x)