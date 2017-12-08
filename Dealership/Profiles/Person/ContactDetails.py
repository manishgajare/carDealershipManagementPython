class ContactDetails:
    __phone_number = ''
    __email = ''

    def __init__(self, phone_number, email):
        self.__phone_number = phone_number
        self.__email = email

    def get_phone_number(self):
        return self.__phone_number

    def get_email(self):
        return self.__email

    def toString(self):
        return 'Phone Number: {}, Email: {}'.format(self.__phone_number,
                                                self.__email)