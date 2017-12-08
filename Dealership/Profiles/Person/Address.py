class Address:
    __street_name = ''
    __block_number = ''
    __city = ''
    __state = ''
    __country = ''
    __zipcode = 0

    def __init__(self, street_name, block_number, city, state, country, zipcode):
        self.__street_name = street_name
        self.__block_number = block_number
        self.__city = city
        self.__state = state
        self.__country = country
        self.__zipcode = zipcode

    def get_street_name(self):
        return self.__street_name

    def get_block_number(self):
        return self.__block_number

    def get_city(self):
        return self.__city

    def get_state(self):
        return self.__state

    def get_country(self):
        return self.__country

    def get_zipcode(self):
        return self.__zipcode

    def toString(self):
        return '{}, {}, {}, {}. {} - {}'.format(self.__street_name,
                                                self.__block_number,
                                                self.__city,
                                                self.__state,
                                                self.__country,
                                                self.__zipcode)