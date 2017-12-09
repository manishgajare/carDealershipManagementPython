class Person:
    __id = ''
    __first_name = ''
    __last_name = ''
    __birth_date = ''
    __income = ''
    __gender = 0
    __address = 0
    __contact_details = 0
    __sensitive_information = 0
    __vehicle_interest = 0

    def __init__(self, id, first_name, last_name, birth_date, income, gender,
                 address, contact_details, sensitive_information, vehicle_interest):
        self.__id = id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__birth_date = birth_date
        self.__income = income
        self.__gender = gender
        self.__address = address
        self.__contact_details = contact_details
        self.__sensitive_information = sensitive_information
        self.__vehicle_interest = vehicle_interest

    def __eq__(self, other):
        return self.get_id() == other.get_id()

    def __ne__(self, other):
            return not self.__eq__(other)

    def __hash__(self):
        return hash(self.__id)

    def get_id(self):
        return self.__id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_birth_date(self):
        return self.__birth_date

    def get_income(self):
        return self.__income

    def get_gender(self):
        return self.__gender

    def get_address(self):
        return self.__address

    def get_contact_details(self):
        return self.__contact_details

    def get_sensitive_information(self):
        return self.__sensitive_information

    def get_vehicle_interest(self):
        return self.__vehicle_interest

    def toString(self):
        return '{} {}\n {}'.format(self.__first_name,
                                   self.__last_name,
                                   self.__address)