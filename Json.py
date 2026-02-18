import json as j



# person_string = {"name":"Barış","Language":["Dutch","English"]}
# print(person_string)
# print(person_string["name"])
# print(person_string["Language"])
# print(person_string["Language"][0])
# print(person_string["Language"][1])




# *********************** JSON String to Dict ***********************
# person_string_json = '{"name":"Barış","Language":["Dutch","English"]}' # JSON formatı


# x = j.loads(person_string_json)
# print(x["name"])
# print(type(x))
# print(x["Language"])
# print(x)

# *********************** JSON String Data'sını yukleme(okuma) ***********************


# with open("person.json","r") as f:
#     x = j.load(f)
#     print(x)
#     print(x["name"])
#     print(x["Language"])
#     print(x["Language"][1])

# *********************** Dict to JSON String ***********************


# person_string_Dict = {"name":"Baris","Language":["Dutch","English"]}

# x = j.dumps(person_string_Dict)
# print(x)
# print(type(x))
# print(x["name"]) # TypeError: string indices must be integers, not 'str' : string'te dict gibi parçalayamayız






# *********************** JSON String Data'sını yazma ***********************


# person_string_Dict = {"name":"Baris","Language":["Dutch","English"]}
# with open("person.json","w") as f:
#     j.dump(person_string_Dict,f)




# *********************** JSON String to Dict formatlama ***********************

# person_string_json = '{"name": "Baris", "Language": ["Dutch", "English"]}'

# x_Dict = j.loads(person_string_json)
# y = j.dumps(x_Dict, indent=2, sort_keys=True)
# print(x_Dict)
# # print(type(x))
# print(y)