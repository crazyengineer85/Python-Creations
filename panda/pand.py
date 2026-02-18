import pandas as pd

# customers ={
#     "customerId": [1,2,3,4],
#     "firstname": ["Ahmet","Ali","asan", "casan"],
#     "Lastname": ["Yılmaz","korkmaz","celik","torpak"]
# }



# order = {

# "customerId": [1,2,5,8],
# "orderıd": [10,11,12,13],
# "ordersdate": ["2025-07-04","2008-07-04","2008-06-04","2008-08-04"]

# }

# dfc = pd.DataFrame(customers,columns=["customerId","firstname","Lastname"])
# dfo = pd.DataFrame(order,columns=["customerId","orderıd","ordersdate"])



# print(f"customers:\n\n{dfc}")
# print(f"order:\n\n{dfo}\n\n")


# x = pd.merge(dfc,dfo,how="inner")
# y = pd.merge(dfc,dfo,how="right")
# z = pd.merge(dfc,dfo,how="left")
# w = pd.merge(dfc,dfo,how="outer")

# print (f"inner:\n\n{x}\nright:\n\n{y}\nleft:\n\n{z}\nouter:\n\n{w}\n")




















customersA = {

"customerId": [1,2,3,4],
"firstname": ["Ahmet","Ali","asan", "casan"],
"Lastname": ["Yılmaz","korkmaz","celik","torpak"]

}
customersB = {

"customerId": [5,6,7,8],
"firstname": ["Aliye","Mine","Seuzan", "Kıymet"],
"Lastname": ["Yılmaz","korkmaz","celik","torpak"]

}

dfca = pd.DataFrame(customersA,columns=["customerId","firstname","Lastname"])
dfcb = pd.DataFrame(customersB,columns=["customerId","firstname","Lastname"])


x = pd.concat([dfca,dfcb],axis=0)

print(x)

y = pd.concat([dfca,dfcb],axis=1)
print(y)