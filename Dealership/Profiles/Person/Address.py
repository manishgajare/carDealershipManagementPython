class Address:
    def __init__(self, street_name, block_number, city, state, country, zipcode):
        self.__street_name = street_name
        self.__block_number = block_number
        self.__city = city
        self.__state = state
        self.__country = country
        self.__zipcode = zipcode

    @property
    def street_name(self):
        return self.__street_name

    @property
    def block_number(self):
        return self.__block_number

    @property
    def city(self):
        return self.__city

    @property
    def state(self):
        return self.__state

    @property
    def country(self):
        return self.__country

    @property
    def zipcode(self):
        return self.__zipcode

    def toString(self):
        return '{}, {}, {}, {}. {} - {}'.format(self.street_name,
                                                self.block_number,
                                                self.city,
                                                self.state,
                                                self.country,
                                                self.zipcode)