#TUPLES - Allows you to create immutable groups of objects. This means that once a tuple is created, it can't be modified. You can't add or remove items.
#uses parantheses instead of square brackets : 
names = ("Roger", "Syd")
names[0] # "Roger"
names[1] # "Syd" - referencing index values


# to heck if an item is contained in a tuple with the in operator:
print("Roger" in names) # True

#to extract a part of a tuple, using slices:
names[0:2] # ('Roger', 'Syd')
names[1:] # ('Syd',)



