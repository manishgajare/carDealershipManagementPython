import threading
from Dealership.Profiles.Person.Address import Address
from Dealership.Profiles.Person.ContactDetails import ContactDetails
from Dealership.Profiles.Person.Person import Person
from Dealership.Profiles.Person.SensitiveInformation import SensitiveInformation
from Dealership.Profiles.Person.VehicleInterest import VehicleInterest


class PersonDirectory:
    __instance = None
    __lock = threading.Lock()

    def __new__(cls):
        if cls.__instance is None:
            with cls.__lock:
                if cls.__instance is None:
                    cls.__instance = super(PersonDirectory, cls).__new__(cls)
                    cls.__instance.__initialized = False
        return cls.__instance

    def __init__(self):
        if self.__initialized:
            return
        self.__person_list = set()
        self.__person_count_for_id = 1
        self.__initialized = True

    @property
    def person_list(self):
        return self.__person_list

    @property
    def person_count_for_id(self):
        return self.__person_count_for_id

    @person_count_for_id.setter
    def person_count_for_id(self, value):
        self.__person_count_for_id = value

    def check_if_exist(self, ssn):
        for person in self.person_list:
            if person.sensitive_information.get_ssn() == ssn:
                return person
        return None

    def add_person(self, first_name, last_name, birth_date, income, gender, street_name, block_number, city, state,
                   country, zipcode, phone_number, email, passport_id, ssn, citizenship_country, vehicle_list):
        existing_person = self.check_if_exist(ssn)
        if existing_person is not None:
            return existing_person

        address = Address(street_name, block_number, city, state, country, zipcode)
        contact_details = ContactDetails(phone_number, email)
        sensitive_information = SensitiveInformation(ssn, passport_id, citizenship_country)
        vehicle_interest = VehicleInterest()
        vehicle_interest.set_vehicle_list(vehicle_list)
        person = Person(self.person_count_for_id, first_name, last_name, birth_date, income, gender,
                        address, contact_details, sensitive_information, vehicle_interest)
        self.person_count_for_id += 1
        self.person_list.add(person)
        return person

    def toString(self):
        person_directory_string = ''
        print('Person Directory -> ')
        for person in self.person_list:
            person_directory_string = person_directory_string + person.toString() + '\n'
        return person_directory_string

