from Dealership.Inventory.VehicleCatalog import VehicleCatalog
from Dealership.Inventory.InventoryCatalog import InventoryCatalog
from Dealership.Profiles.Person.PersonDirectory import PersonDirectory
from Dealership.Profiles.SalesPerson.SalesPersonDirectory import SalesPersonDirectory


class VehicleDealership:

    @staticmethod
    def main():
        from Config import Config
        Config.populate_initial_data()
        VehicleDealership.get_recommendations(26, 'm', 90000)

    @staticmethod
    def add_inventory(quantity_to_add, make, model, year, price, size, color):
        vehicle = VehicleCatalog().add_vehicle(make, model, year, price, size, color)
        return InventoryCatalog().add_inventory_item(vehicle, quantity_to_add)

    @staticmethod
    def create_profile(first_name, last_name, birth_date, income, gender, street_name, block_number, city, state,
                       country, zipcode, phone_number, email, ssn, passport_id, citizenship_country, vehicle_list):
        person_directory = PersonDirectory()
        person = person_directory.check_if_exist(ssn)
        if person is None:
            person = person_directory.add_person(first_name, last_name, birth_date, income, gender, street_name,
                                                 block_number, city, state, country, zipcode, phone_number, email,
                                                 passport_id, ssn, citizenship_country, vehicle_list)
        return person

    @staticmethod
    def get_recommendations(age, gender, income):
        recommendations = SalesPersonDirectory().get_recommendations(age, gender, income)
        for vehicle in recommendations:
            print(vehicle.toString())

if __name__ == '__main__':
    VehicleDealership.main()
