#Assignment operator 
age = 8
#or 
age = 8
anotherVariable = age


#Arithmetic operators 
1 + 1 #2
2 - 1 #1
2 * 2 #4
4 / 2 #2
4 % 3 #1
4 ** 2 #16
4 // 2 #2

#we can also combine them : 
age = 8
age += 1
# age is now 9

#Comparison operators
a = 1
b = 2

a == b #False
a != b #True
a > b #False
a <= b #True


#Boolean operators - not, and, or 
condition1 = True
condition2 = False

not condition1 #False
condition1 and condition2 #False
condition1 or condition2 #True

print(0 or 1) ## 1
print(False or 'hey') ## 'hey'
print('hi' or 'hey') ## 'hi'
print([] or False) ## 'False'
print(False or []) ## '[]'


#Ternary Operator
def is_adult(age):
    if age > 18:
        return True
    else:
        return False


#appending a string using += :
name = "Roger"
name += " is a good dog"

print(name) #Roger is a good dog


#converting a number to a string using the str class constructor
str(8) #"8"
