class Person:
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
        return self.id == other.id

    def __ne__(self, other):
            return not self.__eq__(other)

    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        return '{} {}\n {}'.format(self.first_name,
                                   self.last_name,
                                   self.address.__str__())

    @property
    def id(self):
        return self.__id

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def birth_date(self):
        return self.__birth_date

    @property
    def income(self):
        return self.__income

    @property
    def gender(self):
        return self.__gender

    @property
    def address(self):
        return self.__address

    @property
    def contact_details(self):
        return self.__contact_details

    @property
    def sensitive_information(self):
        return self.__sensitive_information

    @property
    def vehicle_interest(self):
        return self.__vehicle_interest
