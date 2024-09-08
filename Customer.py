from Order import Order


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


customer1 = Customer("Yasir")
customer1.name = "Ali"

print(customer1.name)