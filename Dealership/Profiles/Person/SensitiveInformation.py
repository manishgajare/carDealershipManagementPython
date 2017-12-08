class SensitiveInformation:
    __ssn = ''
    __passport_id = ''
    __citizenship_country = ''

    def __init__(self, ssn, passport_id, citizenship_country):
        self.__ssn = ssn
        self.__passport_id = passport_id
        self.__citizenship_country = citizenship_country

    def get_ssn(self):
        return self.__ssn

    def get_passport_id(self):
        return self.__passport_id

    def get_citizenship_country(self):
        return self.__citizenship_country