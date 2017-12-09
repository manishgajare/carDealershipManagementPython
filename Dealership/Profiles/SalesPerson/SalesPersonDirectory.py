import threading
from Dealership.Invoice.Order.OrderCatalog import OrderCatalog
from Dealership.Profiles.Person.PersonDirectory import PersonDirectory
from Dealership.Profiles.SalesPerson.SalesPerson import SalesPerson
from datetime import datetime, date


class SalesPersonDirectory:
    __instance = None
    __lock = threading.Lock()
    __sales_person_list = None
    __sales_person_count_for_id = None

    def __new__(cls):
        if cls.__instance is None:
            with cls.__lock:
                if cls.__instance is None:
                    cls.__instance = super(SalesPersonDirectory, cls).__new__(cls)
                    cls.__instance.__initialized = False
        return cls.__instance

    def __init__(self):
        if self.__initialized:
            return
        self.__sales_person_list = set()
        self.__sales_person_count_for_id = 1
        self.__initialized = True

    def get_sales_person_list(self):
        return self.__sales_person_list

    def check_if_exist(self, person):
        for sales_person in self.__sales_person_list:
            if sales_person.get_person() == person:
                return sales_person
        return None

    def add_sales_person(self, person):
        existing_sales_person = self.check_if_exist(person)
        if existing_sales_person is not None:
            return existing_sales_person

        sales_person = SalesPerson(self.__sales_person_count_for_id, person)
        self.__sales_person_count_for_id += 1
        self.__sales_person_list.add(sales_person)
        return sales_person

    def get_recommendations(self, age_of_potential_customer, gender_of_potential_customer, income_of_potential_customer):
        person_directory = PersonDirectory()
        order_catalog = OrderCatalog()
        floor_value_for_age = age_of_potential_customer - 3
        ceiling_value_for_age = age_of_potential_customer + 3
        floor_value_for_income = income_of_potential_customer - 15000
        ceiling_value_for_income = income_of_potential_customer + 15000
        vehicle_recommendations = {}

        for person in person_directory.get_person_list():
            if self.check_if_person_falls_in_criteria(person, floor_value_for_age, ceiling_value_for_age, floor_value_for_income,
                                                      ceiling_value_for_income, gender_of_potential_customer):
                for vehicle in person.get_vehicle_interest().get_vehicle_list():
                    if vehicle in vehicle_recommendations:
                        vehicle_recommendations[vehicle] = vehicle_recommendations.get(vehicle) + 10
                    else:
                        vehicle_recommendations[vehicle] = 10

        for order in order_catalog.get_order_list():
            person = order.get_customer().get_person()
            if self.check_if_person_falls_in_criteria(person, floor_value_for_age, ceiling_value_for_age, floor_value_for_income,
                                                      ceiling_value_for_income, gender_of_potential_customer):
                for order_item in order.get_order_item_list():
                    vehicle = order_item.get_inventory_item().get_vehicle()
                    if vehicle in vehicle_recommendations:
                        vehicle_recommendations[vehicle] = vehicle_recommendations.get(vehicle) + 20
                    else:
                        vehicle_recommendations[vehicle] = 20

        sorted_recommendations_by_points = sorted(vehicle_recommendations, key=vehicle_recommendations.get, reverse=True)
        top_recommendations = sorted_recommendations_by_points[:5]
        # sorting by price
        top_recommendations.sort(key=lambda x: x.price, reverse=True)
        return top_recommendations

    def check_if_person_falls_in_criteria(self, person, floor_value_for_age, ceiling_value_for_age, floor_value_for_income,
                                          ceiling_value_for_income, gender_of_potential_customer):
        age_of_person = self.calculate_age(person.get_birth_date())
        income_of_person = person.get_income()
        if gender_of_potential_customer == person.get_gender() \
                and floor_value_for_income <= income_of_person <= ceiling_value_for_income \
                and floor_value_for_age <= age_of_person <= ceiling_value_for_age:
            return True
        return False

    def calculate_age(self, birth_date):
        today = date.today()
        return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    def toString(self):
        sales_person_directory_string = ''
        print('Sales Person Directory -> ')
        for sales_person in self.__sales_person_list:
            sales_person_directory_string = sales_person_directory_string + sales_person.toString() + '\n'
        return sales_person_directory_string
