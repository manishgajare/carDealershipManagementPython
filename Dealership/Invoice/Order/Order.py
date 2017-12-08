from Dealership.Inventory.InventoryCatalog import InventoryCatalog
from Dealership.Invoice.Order.OrderItem import OrderItem


class Order:
    __id = 0
    __order_item_list = None
    __customer = None
    __sales_person = None
    __order_item_count_for_id = 0

    def __init__(self, id, customer, sales_person):
        self.__id = id
        self.__customer = customer
        self.__sales_person = sales_person
        self.__order_item_list = set()
        self.__order_item_count_for_id = 1

    def get_id(self):
        return self.__id

    def get_customer(self):
        return self.__customer

    def get_sales_person(self):
        return self.__sales_person

    def get_order_item_list(self):
        return self.__order_item_list

    def add_order_item(self, inventory_item, price):
        order_item = OrderItem(self.__order_item_count_for_id, inventory_item, price)
        self.__order_item_count_for_id += 1
        InventoryCatalog().remove_inventory_item(inventory_item, 1)
        self.__order_item_list.add(order_item)
        return order_item

    def toString(self):
        return 'id: {}, customer: {}, sales person: {}, order item list: {}'.format(self.__id,
                                                                                    self.__customer,
                                                                                    self.__sales_person,
                                                                                    self.__order_item_list)