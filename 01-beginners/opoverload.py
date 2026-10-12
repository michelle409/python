#OPERATOR OVERLOADING - o make classes comparable and to make them work with python operators
class Dog:
    # the Dog class
    def __init__(self, name, age):
        self.name = name
        self.age = age
roger = Dog('Roger', 8)
syd = Dog('Syd', 7)

#using operator overloading to add a way to compare those 2 objects, based on the age property
class Dog:
    # the Dog class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __gt__(self, other):
        return True if self.age > other.age else False
