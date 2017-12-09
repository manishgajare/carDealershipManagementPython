class InventoryItem:
    __id = 0
    __vehicle = None
    __price = 0
    __quantity_available = 0

    def __init__(self, id, vehicle, price, quantity_available):
        self.__id = id
        self.__vehicle = vehicle
        self.__price = price * 1.1
        self.__quantity_available = quantity_available

    def __eq__(self, other):
        return self.get_id() == other.get_id()

    def __ne__(self, other):
            return not self.__eq__(other)

    def __hash__(self):
        return hash(self.__id)

    def get_id(self):
        return self.__id

    def get_vehicle(self):
        return self.__vehicle

    def get_price(self):
        return self.__price

    def get_quantity_available(self):
        return self.__quantity_available

    def set_price(self, price):
        self.__price = price * 1.1

    def increment_quantity_available(self, quantity_to_be_added):
        self.__quantity_available = self.__quantity_available + quantity_to_be_added

    def decrement_quantity_available(self, quantity_to_be_removed):
        self.__quantity_available = self.__quantity_available - quantity_to_be_removed

    def toString(self):
        return 'id: {}, price: {}, quantity available: {}, vehicle -> {}'.format(self.__id,
                                                                                 self.__price,
                                                                                 self.__quantity_available,
                                                                                 self.__vehicle.toString())