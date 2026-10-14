#tuple : ordered, immutable, allows duplicate elements 
#main diff from lists - cannot be changed afte rmaking it
"""mytuple = ("max", 28, "boston")
print(mytuple)
#always written with or without (), 

#to print just one element : add a coma at the end
mytuple = ("max",)
print(mytuple) 
print(type(mytuple))

#to create a tuple from an interable: 
mytuple = tuple(["max", 28, "boston"])
print(mytuple)

#to access elements - index values
item = mytuple[1]
print (item)
#another way of printing the last element -  0,-1,-2
item = mytuple[-2]
print (item) """

#to print ecah element
"""mytuple = ("max", 28, "boston")
for i in mytuple:
    print(i)

if "max" in mytuple:
    print("yes")
else :
    print("no") """

#to get the length of the tuple
"""mytuple = ("max", 28, "boston")
print(len(mytuple))

#to count the no.of elements in a tuple 
mytuple = ("max", 28, "boston")
print(mytuple.count("max"))

#to check the position of an element:
mytuple = ("max", 28, "boston")
print(mytuple.index("max")) #returns the first occurence

#to convert tuple to a function
mylist = list(mytuple)
print(mylist)
mytuple2 = tuple(mylist)


#slicing w tuples
a = (1,2,3,4,5,6,7,8,9,10)
b = a[2:5] #doesnt include the 5th index value
print(b)"""

#unpacking
"""mytuple = ("max", 28, "boston")
name,age,city = mytuple
print(name)
print(age)
print(city)"""

mytuple = (0,1,2,3,4)
i1, *i2, i3 = mytuple  
print(i2) #* always collects into a list, even if you’re unpacking a tuple
#logic : i1 gets the first value → 0
#        i3 gets the last value → 4
#       *i2 gets everything in between → [1, 2, 3]