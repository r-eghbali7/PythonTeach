# Data structure type ---- انواع داده 
# dictionry
# انواع داده سطح ۱
# {}    dict()      key     valuble     change valuble      append key      items()     valuese()       keys()

# {}     کلید ها نباید تکراری باشد
dict1 = {"a":2 , "b":33 , "c":"best"}
print(type(dict1),"___",dict1)
print("a:",dict1["a"])

print(40*"-")

# dict()
dict2 = dict([("name","ali") , ("family","azadi") , ("age",20)])
print(type(dict2), "___" , dict2)
print("family:" , dict2["family"])

dict2_new = dict([("name","ali") ,
     
                  ("family","azadi") , 
     
                  ("age",20)
                ])

print("dict_new:",dict2_new)

print(40*("-"))

dict3 = dict(q = 9 , w = 8 , e = 7 )
print(type(dict3),"___",dict3)
print("e:" , dict3["e"])

print(40*"-")

# change valuble
dict4 = {"name_d":"mostafa","family:":"salime","age":20}
print(dict4,"\n") 
dict4["family:"]= "samney"
dict4["age"]=23
print(dict4)

print(40*"-")

# append key
dict5 = dict(vahed = "manabe" , tabghe = 20 )
dict5["name_room"] = "modir"
print(dict5)

print(40*"-")

# items()     valuese()       keys()
dict6 = {"name_d":"mostafa","family:":"salime","age":20}
print(type(dict6),"___",dict6.items())
print(type(dict6),"___",dict6.values())
print(type(dict6),"___",dict6.keys())

print("-------------------")
print(sorted(dict6))
