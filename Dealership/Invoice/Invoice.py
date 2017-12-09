class Invoice:
    __id = 0
    __order = None
    __price = 0

    def __init__(self, id, order):
        self.__id = id
        self.__order = order
        for order_item in order.get_order_item_list():
            self.__price += order_item.get_price()

    def __eq__(self, other):
        return self.get_id() == other.get_id()

    def __ne__(self, other):
            return not self.__eq__(other)

    def __hash__(self):
        return hash(self.__id)

    def get_id(self):
        return self.__id

    def get_order(self):
        return self.__order

    def get_price(self):
        return self.__price

    def toString(self):
        return 'id: {}, order: {}, price: {}'.format(self.__id, self.__order, self.__price)