#CLASSES - An object is an instance of a class. A class is the type of an object.
class Dog:
    # the Dog class

#defining methods : 
class Dog:
    # the Dog class

roger = Dog() #new object of type Dog
print(type(roger))

#constructor -  to initialize one or more properties when we create a new object from that class

class Dog:
    # the Dog class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print('WOF!')

#inheritance - imp class feature : 
class Animal:
    def walk(self):
        print('Walking..')
#dog class inherting :
class Dog(Animal):
    def bark(self):
        print('WOF!')
roger = Dog()
roger.walk() # 'Walking..'
roger.bark() # 'WOF!'


