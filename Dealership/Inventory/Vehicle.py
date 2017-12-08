class Vehicle:
    __id = 0
    __make = None
    __model = ''
    __year = 0
    __price = 0
    __size = None
    __color = None

    def __init__(self, id, make, model, year, price, size, color):
        self.__id = id
        self.__make = make
        self.__model = model
        self.__year = year
        self.__price = price
        self.__size = size
        self.__color = color

    def get_id(self):
        return self.__id

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_size(self):
        return self.__size

    def get_color(self):
        return self.__color

    def toString(self):
        return 'id: {}, make: {}, model: {}, year: {}, price: {}, size: {}, color: {}'.format(self.__id,
                                                                                              self.__make,
                                                                                              self.__model,
                                                                                              self.__year,
                                                                                              self.__price,
                                                                                              self.__size,
                                                                                              self.__color)