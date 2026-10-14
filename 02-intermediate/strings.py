"""mystr= 'hello world'
mystr=mystr.strip() # to remoeve the extra spaces
print(mystr)

#to check if its in lower or upper case :
print(mystr.lower())
print(mystr.upper())
print(mystr.startswith('hello'))
print(mystr.endswith('hello'))

print(mystr.find('o')) #to find where the letter is 

#to replace 
print(mystr.replace('world', 'universe'))


mystr1='how are u doing'
mylist=mystr.split()
print(mylist)


mystr='how,are,you,doing'
mylist=mystr.split(",")
print(mylist)

mystr='how,are,you,doing'
mylist=mystr.split(",")
newstr=' '.join(mylist)
print(newstr)

mylist=['a']*6
print(mylist)
mystg=''.join(mylist)
print(mystg)"""




#formatting strings - %, format(), f-strings
var="tom"
mystr="the variable is %s" % var
print(mystr)

#format() method 
var=3.4765487
mystr="the variable is {:.4f}".format(var)
print(mystr)           #this shows upto how many decimal places

#fstring method 
var=3.4765487
name ='tom'
mystr=f"the variable is {var} and name is {name}"
print(mystr)           