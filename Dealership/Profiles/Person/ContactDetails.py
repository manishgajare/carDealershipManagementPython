class ContactDetails:
    def __init__(self, phone_number, email):
        self.__phone_number = phone_number
        self.__email = email

    @property
    def phone_number(self):
        return self.__phone_number

    @property
    def email(self):
        return self.__email

    def toString(self):
        return 'Phone Number: {}, Email: {}'.format(self.phone_number,
                                                self.email)