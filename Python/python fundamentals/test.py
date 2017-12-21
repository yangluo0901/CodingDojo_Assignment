dict1 = {"name":"yangLuo","age":"26", "gender":"male"}
value =["mickey",100, "female"]
# print dict.items()
# print dict.iteritems()
dict2 = dict.fromkeys(dict1,element for element in value)
print dict2
