class SensitiveInformation:
    __ssn = ''
    __passport_id = ''
    __citizenship_country = ''

    def __init__(self, ssn, passport_id, citizenship_country):
        self.__ssn = ssn
        self.__passport_id = passport_id
        self.__citizenship_country = citizenship_country

    @property
    def ssn(self):
        return self.__ssn

    @property
    def passport_id(self):
        return self.__passport_id

    @property
    def citizenship_country(self):
        return self.__citizenship_country