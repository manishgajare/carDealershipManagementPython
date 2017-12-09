class InventoryItem:
    def __init__(self, id, vehicle, price, quantity_available):
        self.__id = id
        self.__vehicle = vehicle
        self.__price = price * 1.1
        self.__quantity_available = quantity_available

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
    def vehicle(self):
        return self.__vehicle

    @property
    def price(self):
        return self.__price

    @property
    def quantity_available(self):
        return self.__quantity_available

    @price.setter
    def price(self, price):
        self.__price = price * 1.1

    @quantity_available.setter
    def quantity_available(self, value):
        self.__quantity_available = value

    def toString(self):
        return 'id: {}, price: {}, quantity available: {}, vehicle -> {}'.format(self.id,
                                                                                 self.price,
                                                                                 self.quantity_available,
                                                                                 self.vehicle.toString())