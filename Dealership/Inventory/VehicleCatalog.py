import threading
from Dealership.Inventory.InventoryCatalog import InventoryCatalog
from Dealership.Inventory.Vehicle import Vehicle


class VehicleCatalog:
    __instance = None
    __lock = threading.Lock()

    def __new__(cls):
        if cls.__instance is None:
            with cls.__lock:
                if cls.__instance is None:
                    cls.__instance = super(VehicleCatalog, cls).__new__(cls)
                    cls.__instance.__initialized = False
        return VehicleCatalog.__instance

    def __init__(self):
        if self.__initialized:
            return
        self.__vehicle_list = set()
        self.__vehicle_count_for_id = 1
        self.__initialized = True

    def __str__(self):
        vehicle_catalog_string = 'Vehicle Catalog -> \n'
        for vehicle in self.vehicle_list:
            vehicle_catalog_string = vehicle_catalog_string + vehicle.__str__() + '\n'
        return vehicle_catalog_string

    @property
    def vehicle_list(self):
        return self.__vehicle_list

    @property
    def vehicle_count_for_id(self):
        return self.__vehicle_count_for_id

    @vehicle_count_for_id.setter
    def vehicle_count_for_id(self, value):
        self.__vehicle_count_for_id = value

    def check_if_exist(self, vehicle_make, vehicle_size, vehicle_color, year, model):
        for vehicle in self.vehicle_list:
            if vehicle.make == vehicle_make and \
                    vehicle.size == vehicle_size and \
                    vehicle.color == vehicle_color and \
                    vehicle.year == year and \
                    vehicle.model == model:
                return vehicle
        return None

    def add_vehicle(self, make, model, year, price, size, color):
        existing_vehicle = self.check_if_exist(make, size, color, year, model)
        if existing_vehicle is not None:
            print('Vehicle already exist')
            if existing_vehicle.price != price:
                existing_vehicle.set_price(price)
                InventoryCatalog().check_if_exist(existing_vehicle).set_price(price)
                print('updated price for existing vehicle', existing_vehicle)
            return existing_vehicle

        v = Vehicle(self.__vehicle_count_for_id, make, model, year, price, size, color)
        self.vehicle_count_for_id += 1
        self.vehicle_list.add(v)
        print('Vehicle added to Vehicle Catalog')
        return v
