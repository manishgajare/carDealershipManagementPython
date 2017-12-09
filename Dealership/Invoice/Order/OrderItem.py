class OrderItem:
    def __init__(self, id, inventory_item, price):
        self.__id = id
        self.__inventory_item = inventory_item
        self.__price = price

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
            return not self.__eq__(other)

    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        return 'id: {}, inventory item: {}, price: {}'.format(self.id, self.inventory_item.__str__(), self.price)

    @property
    def id(self):
        return self.__id

    @property
    def inventory_item(self):
        return self.__inventory_item

    @property
    def price(self):
        return self.__price
