from Dealership.Inventory.InventoryCatalog import InventoryCatalog
from Dealership.Invoice.Order.OrderItem import OrderItem


class Order:
    def __init__(self, id, customer, sales_person):
        self.__id = id
        self.__customer = customer
        self.__sales_person = sales_person
        self.__order_item_list = set()
        self.__order_item_count_for_id = 1

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
            return not self.__eq__(other)

    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        order_items_string = ''
        for order_item in self.order_item_list:
            order_items_string += order_item.__str__()
        return 'id: {}, customer: {}, sales person: {}, \nOrder Items -> {}'.format(self.id,
                                                                                    self.customer.__str__(),
                                                                                    self.sales_person.__str__(),
                                                                                    order_items_string)

    @property
    def id(self):
        return self.__id

    @property
    def customer(self):
        return self.__customer

    @property
    def sales_person(self):
        return self.__sales_person

    @property
    def order_item_list(self):
        return self.__order_item_list

    @property
    def order_item_count_for_id(self):
        return self.__order_item_count_for_id

    @order_item_count_for_id.setter
    def order_item_count_for_id(self, value):
        self.__order_item_count_for_id = value

    def add_order_item(self, inventory_item, price):
        order_item = OrderItem(self.order_item_count_for_id, inventory_item, price)
        self.order_item_count_for_id += 1
        InventoryCatalog().decrement_inventory_quantity(inventory_item, 1)
        self.order_item_list.add(order_item)
        return order_item
