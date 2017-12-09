import threading

from Dealership.Invoice.Order.Order import Order


class OrderCatalog:
    __instance = None
    __lock = threading.Lock()

    def __new__(cls):
        if cls.__instance is None:
            with cls.__lock:
                if cls.__instance is None:
                    cls.__instance = super(OrderCatalog, cls).__new__(cls)
                    cls.__instance.__initialized = False
        return cls.__instance

    def __init__(self):
        if self.__initialized:
            return
        self.__order_list = set()
        self.__order_count_for_id = 1
        self.__initialized = True

    def __str__(self):
        order_catalog_string = 'Order Catalog -> \n'
        for order in self.order_list:
            order_catalog_string = order_catalog_string + order.__str__() + '\n'
        return order_catalog_string

    @property
    def order_list(self):
        return self.__order_list

    @property
    def order_count_for_id(self):
        return self.__order_count_for_id

    @order_count_for_id.setter
    def order_count_for_id(self, value):
        self.__order_count_for_id = value

    def add_order(self, customer, sales_person, inventory_item, price):
        order = Order(self.order_count_for_id, customer, sales_person)
        self.order_count_for_id += 1
        order.add_order_item(inventory_item, price)
        self.order_list.add(order)
        return order
