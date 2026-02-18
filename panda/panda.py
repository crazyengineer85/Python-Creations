import pandas as pd



# customers = {

# "customerId": [1,2,3,4],
# "firstname": ["Ahmet","Ali","asan", "casan"],
# "Lastname": ["Yılmaz","korkmaz","celik","torpak"]

# }



# order = {

# "customerId": [1,2,5,8],
# "orderıd": [10,11,12,13],
# "ordersdate": ["2025-07-04","2008-07-04","2008-06-04","2008-08-04"]

# }


# dfc = pd.DataFrame(customers, columns=["customerId","firstname","Lastname"])
# dfo = pd.DataFrame(order, columns=["customerId","orderıd","ordersdate"])
# print(dfc)
# print(dfo)

# x = pd.merge(dfc,dfo,how="inner")
# x = pd.merge(dfc,dfo,how="left")
# x = pd.merge(dfc,dfo,how="right")

# print(x)

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

# dfc = pd.DataFrame(customersA, columns=["customerId","firstname","Lastname"])
# dfq = pd.DataFrame(customersB, columns=["customerId","firstname","Lastname"])


# # x = pd.concat([customersA,customersB])
# x = pd.concat([dfc,dfq],axis=1)
# print(x)