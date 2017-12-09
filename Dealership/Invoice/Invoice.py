class Invoice:
    def __init__(self, id, order):
        self.__id = id
        self.__order = order
        self.__price = 0
        for order_item in order.order_item_list:
            self.__price += order_item.price

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
            return not self.__eq__(other)

    def __hash__(self):
        return hash(self.id)

    @property
    def id(self):
        return self.__id

    @property
    def order(self):
        return self.__order

    @property
    def price(self):
        return self.__price

    def toString(self):
        return 'id: {}, order: {}, price: {}'.format(self.id, self.order, self.price)