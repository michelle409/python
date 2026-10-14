#dictionary - key-value pairs, mutable, unordered
#made with {}
"""mydict = {"name": "max", "age": 28, "city": "new york"}
print(mydict)

mydict2= dict(name="mary", age=27, city="boston")
print(mydict2) #no qoutes needed for the keys

#to access the values
value = mydict["name"] #key name
print(value)

#to add a new key
mydict["email"] = "abc"
print(mydict)

#to delete a key
del mydict["name"]
print(mydict)
 #or using pop
mydict.pop("age")
print(mydict)"""

#to checek if an element is in the dict
"""mydict = {"name": "max", "age": 28, "city": "new york"}
print(mydict)
if "name" in mydict :
    print(mydict["name"])
else :
    print("error")

#using try except method
try:
    print(mydict("lastname"))
except :
    print("error")

#to loop key : 
for key in mydict:
    print(key)

#to loop values :
for value in mydict.values():
    print(value)

#to loop both :
for key, value in mydict.items():
    print(key,value) """

#to copy a dict
"""mydict = {"name": "max", "age": 28, "city": "new york"}
mydict_cpy = mydict
print(mydict_cpy)

mydict_cpy["email"] = "abc"
print(mydict_cpy)
print(mydict) #both have same values

#to copy without modifying th eoriginal one :
mydict_copy =mydict.copy()
#or
mydict_copy =dict(mydict)"""

#updtight method - to combine two dicts
mydict = {"name": "max", "age": 28, "city": "new york", "email" : "abc"}
mydict2 = {"name": "mary", "age": 27, "city": "boston"}
mydict.update(mydict2)
print(mydict)