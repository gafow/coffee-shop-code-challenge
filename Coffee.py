from Order import Order

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


