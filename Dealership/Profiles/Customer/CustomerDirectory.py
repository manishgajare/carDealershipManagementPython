import threading

from Dealership.Profiles.Customer.Customer import Customer


class CustomerDirectory:
    __instance = None
    __lock = threading.Lock()
    __customer_list = None
    __customer_count_for_id = None

    def __new__(cls):
        if cls.__instance is None:
            with cls.__lock:
                if cls.__instance is None:
                    cls.__instance = super(CustomerDirectory, cls).__new__(cls)
                    cls.__instance.__initialized = False
        return cls.__instance

    def __init__(self):
        if self.__initialized:
            return
        self.__customer_list = set()
        self.__customer_count_for_id = 1
        self.__initialized = True

    def get_customer_list(self):
        return self.__customer_list

    def check_if_exist(self, person):
        for customer in self.__customer_list:
            if customer.get_person() == person:
                return customer
        return None

    def add_cutomer(self, person):
        existing_customer = self.check_if_exist(person)
        if existing_customer is not None:
            return existing_customer

        customer = Customer(self.__customer_count_for_id, person)
        self.__customer_count_for_id += 1
        self.__customer_list.add(customer)
        return customer

    def toString(self):
        customer_directory_string = ''
        print('Customer Directory -> ')
        for customer in self.__customer_list:
            customer_directory_string = customer_directory_string + customer.toString() + '\n'
        return customer_directory_string
