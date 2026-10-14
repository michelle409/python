#slicing
"""mylist = [1,2,3,4,5,6,7,8,9,]
a=mylist[1:5]
print (a) 

#step slicing
mylist = [1,2,3,4,5,6,7,8,9,]
a=mylist[1::2] #from first element and taking every second element
print (a) 

mylist = [1,2,3,4,5,6,7,8,9,]
a=mylist[1::4] #from first element and taking every fourth element
print (a)

#reversing a list :
mylist = [1,2,3,4,5,6,7,8,9,]
a=mylist[::-1]
print (a) """


"""list_org = ["banana", "cherry", "apple"]
list_cpy = list_org
list_cpy.append("lemon")
print(list_org) #if u appened an elemnet to the copy it will get modified in the original list too.
print(list_cpy)

#method 1 : to keep the original list same use: .copy()
list_org = ["banana", "cherry", "apple"]
list_cpy = list_org.copy()
list_cpy.append("lemon")
print(list_org) 
print(list_cpy)

#method 2 : using the list function :
list_org = ["banana", "cherry", "apple"]
list_cpy = list(list_org)
list_cpy.append("lemon")
print(list_org) 
print(list_cpy)

#method 3 : using slicing 
list_org = ["banana", "cherry", "apple"]
list_cpy = list_org[:] #slicng all the way from the begining to the end
list_cpy.append("lemon")
print(list_org) 
print(list_cpy)"""

#list comprehension - fast way to create a new list from an esisting list
mylist= [1,2,3,4,5,6]
b=[i*i for i in mylist]
print(mylist)
print(b)