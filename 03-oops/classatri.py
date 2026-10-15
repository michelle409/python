class item:
    payrate = 0.8

    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0
        assert quantity >= 0
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def applydiscount(self):
        self.price = self.price * self.payrate  # self.payrate not item.payrate


item1 = item("phone", 100, 1)
item1.applydiscount()
print(item1.price)  # 80.0

item2 = item("laptop", 1000, 3)
item2.payrate = 0.7  # override payrate for this instance only
item2.applydiscount()
print(item2.price)  # 700.0

print(item.__dict__)   # class level
print(item1.__dict__)  # instance level