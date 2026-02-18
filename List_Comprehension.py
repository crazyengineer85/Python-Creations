
# for ve while dongu alternatifi


# for x in range(5,10):
#     print(x)

# number =[x for x in range(5,10)]
# print(number)





# number = []
# for x in range(10):
#     number.append(x)
# print(number)

# number = [x*x for x in range(10) if x%3==0]

# print(number)


# a = [x if x%2==0 else 'tek' for x in range(1,10)]
# print(a)

z = []
for x in range(5):
    for y in range(5):
        z.append((x,y))
print(z)





number = [(x,y) for x in range(5) for y in range(5)]
print(number)