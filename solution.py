# CUSTOMER CLASS

class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
            
    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    def orders(self):
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        all_coffees = [ order.coffee for order in Order.all if order.customer == self ]
        unique_coffees = set(all_coffees)
        result_list = list(unique_coffees)
        return result_list

# COFFEE CLASS

class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 3 <= len(value) and not hasattr(self, 'name'):
            self._name = value

    def orders(self):
        return [order for order in Order.all if order.coffee == self]

    def customers(self):
        all_customers = [
            order.customer for order in Order.all if order.coffee == self]
        unique_customers = set(all_customers)
        result_list = list(unique_customers)
        return result_list

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        return sum([ order.price for order in self.orders() ])/len(self.orders())

# ORDER CLASS

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




