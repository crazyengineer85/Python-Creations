# def square(x): return x**2

# x = square(8)
# print(x)



# def square(x): return x**2

# number = [1,2,3,4,5]
# # x = list(map(square, number))
# x = tuple(map(square, number))
# print(x)

# def square(x): return x**2

# number = [1,2,3,4,5]
# # x = list(map(square, number))
# x = list(map(square, number))

# for i in x:
#     print(i)


# def square(x): return x**2

# # number = [1,2,3,4,5]
# # # x = list(map(square, number))
# # x = list(map(square, number))

# # for i in x:
# #     print(i)


# def check_even(x): return x%2==0

# number =[1,2,3,4,5,6,7,8]

# x = list(filter(check_even, number))
# print(x)





# number =[1,2,3,4,5,6,7,8]

# x = list(filter(lambda x: x%2==0, number))
# print(x)

w = lambda x: x%2==0
number =[1,2,3,4,5,6,7,8]

x = list(filter(w, number))
print(x)