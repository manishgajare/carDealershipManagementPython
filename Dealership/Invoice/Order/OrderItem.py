class OrderItem:
    __id = 0
    __inventory_item = None
    __price = 0

    def __init__(self, id, inventory_item, price):
        self.__id = id
        self.__inventory_item = inventory_item
        self.__price = price

    def __eq__(self, other):
        return self.get_id() == other.get_id()

    def __ne__(self, other):
            return not self.__eq__(other)

    def __hash__(self):
        return hash(self.__id)

    def get_id(self):
        return self.__id

    def get_inventory_item(self):
        return self.__inventory_item

    def get_price(self):
        return self.__price

    def toString(self):
        return 'id: {}, inventory item: {}, price: {}'.format(self.__id, self.__inventory_item, self.__price)