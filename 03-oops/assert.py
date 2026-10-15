class item :
    def __init__(self, name:str,price:float,quantity=0):
        #run validations to the received arguments 
        assert price>=0, f"price{price} is not greater than or equal to  0"
        assert quantity >=0, f"price{quantity} is not greater than or equal to 0"



        #assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        

    def calculate_total_price(self) :  #methods are functions which are inside the class
        return self.price * self.quantity 



item1=item("phone",100,-1)
item2=item("laptop", 1000,3)


print(item1.calculate_total_price())
print(item2.calculate_total_price())
