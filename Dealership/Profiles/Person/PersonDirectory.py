import threading
from Dealership.Profiles.Person.Address import Address
from Dealership.Profiles.Person.ContactDetails import ContactDetails
from Dealership.Profiles.Person.Person import Person
from Dealership.Profiles.Person.SensitiveInformation import SensitiveInformation
from Dealership.Profiles.Person.VehicleInterest import VehicleInterest


class PersonDirectory:
    __instance = None
    __lock = threading.Lock()
    __person_list = None
    __person_count_for_id = None

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

    def get_person_list(self):
        return self.__person_list

    def check_if_exist(self, ssn):
        for person in self.__person_list:
            if person.get_sensitive_information().get_ssn() == ssn:
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
        person = Person(self.__person_count_for_id, first_name, last_name, birth_date, income, gender,
                        address, contact_details, sensitive_information, vehicle_interest)
        self.__person_count_for_id += 1
        self.__person_list.add(person)
        return person

    def toString(self):
        person_directory_string = ''
        print('Person Directory -> ')
        for person in self.__person_list:
            person_directory_string = person_directory_string + person.toString() + '\n'
        return person_directory_string

