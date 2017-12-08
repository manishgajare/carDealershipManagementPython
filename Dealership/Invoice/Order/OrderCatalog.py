import threading

from Dealership.Invoice.Order.Order import Order


class OrderCatalog:
    __instance = None
    __lock = threading.Lock()
    __order_list = None
    __order_count_for_id = None

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

    def get_order_list(self):
        return self.__order_list

    def add_order(self, customer, sales_person, inventory_item, price):
        order = Order(self.__order_count_for_id, customer, sales_person)
        self.__order_count_for_id += 1
        order.add_order_item(inventory_item, price)
        self.__order_list.add(order)
        return order

    def toString(self):
        order_catalog_string = ''
        print('Order Catalog -> ')
        for order in self.__order_list:
            order_catalog_string = order_catalog_string + order.toString() + '\n'
        return order_catalog_string