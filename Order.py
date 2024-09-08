from Customer import Customer
from Coffee import Coffee

class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if (not hasattr(self, 'price') and isinstance(price, float)
            and 1 <= price <= 10):
            self._price = price

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        if isinstance(value, Customer):
            self._customer = value


customer = Customer("Yasir")
coffee = Coffee("Flat White")
order = Order(customer, coffee, 2.5)

print(order.coffee.name)