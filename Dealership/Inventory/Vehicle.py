class Vehicle:
    def __init__(self, id=0, make=None, model='', year=0, price=0, size=None, color=None):
        self.__id = id
        self.__make = make
        self.__model = model
        self.__year = year
        self.__price = price
        self.__size = size
        self.__color = color

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
    def make(self):
        return self.__make

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    @property
    def price(self):
        return self.__price

    @property
    def size(self):
        return self.__size

    @property
    def color(self):
        return self.__color

    @price.setter
    def price(self, price):
        self.__price = price

    def toString(self):
        return 'id: {}, make: {}, model: {}, year: {}, price: {}, size: {}, color: {}'.format(self.id,
                                                                                              self.make,
                                                                                              self.model,
                                                                                              self.year,
                                                                                              self.price,
                                                                                              self.size,
                                                                                              self.color)