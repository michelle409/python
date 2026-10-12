#while loop - while loops are defined using the while keyword, and they repeat their block until the condition is evaluated as False.
condition = True
while condition == True:
    print("The condition is True")
    condition = False

print("After the loop")
count = 0
while count < 10:
    print("The condition is True")
    count = count + 1

print("After the loop")


#for loop
items = [1, 2, 3, 4]
for item in items:
    print(item)

#by giving a range : 
for item in range(04):
    print(item)

#To get the index, you should wrap the sequence into the enumerate() function.
items = [1, 2, 3, 4]
for index, item in enumerate(items):
    print(index, item)


#break - to intterupt while and for loops inside the block
items = [1, 2, 3, 4]
for item in items:
    if item == 2:
        break
    print(item)

#continue - to intterupt while and for loops inside the block
items = [1, 2, 3, 4]
for item in items:
    if item == 2:
        continue
    print(item)
