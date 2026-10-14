class item :
    def __init__(self, name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self) :  #methods are functions which are inside the class
        return self.price*self.quantity 



item1=item("phone",100,5)
item2=item("laptop", 1000,3)


print(item1.calculate_total_price())
print(item2.calculate_total_price())
