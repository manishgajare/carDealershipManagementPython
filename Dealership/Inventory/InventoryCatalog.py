from Dealership.Inventory.VehicleFeatures.VehicleSize import VehicleSize
from Dealership.Inventory.InventoryItem import InventoryItem
import threading


class InventoryCatalog:
    __instance = None
    __lock = threading.Lock()

    def __new__(cls):
        if cls.__instance is None:
            with cls.__lock:
                if cls.__instance is None:
                    cls.__instance = super(InventoryCatalog, cls).__new__(cls)
                    cls.__instance.__initialized = False
        return cls.__instance

    def __init__(self):
        if self.__initialized:
            return
        self.__SMALL_TOTAL_INVENTORY_SPACE = 180
        self.__MEDIUM_TOTAL_INVENTORY_SPACE = 170
        self.__LARGE_TOTAL_INVENTORY_SPACE = 150
        self.__small_available_inventory_space = self.__SMALL_TOTAL_INVENTORY_SPACE
        self.__medium_available_inventory_space = self.__MEDIUM_TOTAL_INVENTORY_SPACE
        self.__large_available_inventory_space = self.__LARGE_TOTAL_INVENTORY_SPACE
        self.__inventory_list = set()
        self.__inventory_count_for_id = 1
        self.__initialized = True

    @property
    def inventory_list(self):
        return self.__inventory_list

    @property
    def small_available_inventory_space(self):
        return self.__small_available_inventory_space

    @property
    def medium_available_inventory_space(self):
        return self.__medium_available_inventory_space

    @property
    def large_available_inventory_space(self):
        return self.__large_available_inventory_space

    @property
    def small_total_inventory_space(self):
        return self.__SMALL_TOTAL_INVENTORY_SPACE

    @property
    def medium_total_inventory_space(self):
        return self.__MEDIUM_TOTAL_INVENTORY_SPACE

    @property
    def larger_total_inventory_space(self):
        return self.__LARGE_TOTAL_INVENTORY_SPACE

    @property
    def inventory_count_for_id(self):
        return self.__inventory_count_for_id

    @inventory_count_for_id.setter
    def inventory_count_for_id(self, value):
        self.__inventory_count_for_id = value

    @small_available_inventory_space.setter
    def small_available_inventory_space(self, value):
        self.__small_available_inventory_space = value

    @medium_available_inventory_space.setter
    def medium_available_inventory_space(self, value):
        self.__medium_available_inventory_space = value

    @large_available_inventory_space.setter
    def large_available_inventory_space(self, value):
        self.__large_available_inventory_space = value

    def check_if_exist(self, vehicle):
        for item in self.inventory_list:
            if item.vehicle == vehicle:
                return item
        return None

    def check_if_enough_space_to_add_inventory(self, vehicle_size, quantity_to_add):
        is_available = False
        if ((vehicle_size == VehicleSize.SMALL and quantity_to_add <= self.small_available_inventory_space) or
                (vehicle_size == VehicleSize.MEDIUM and quantity_to_add <= self.medium_available_inventory_space) or
                (vehicle_size == VehicleSize.LARGE and quantity_to_add <= self.large_available_inventory_space)):
            is_available = True
        return is_available

    def increment_available_space(self, vehicle_size, quantity):
        if vehicle_size == VehicleSize.SMALL:
            self.small_available_inventory_space += quantity
        elif vehicle_size == VehicleSize.MEDIUM:
            self.medium_available_inventory_space += quantity
        elif vehicle_size == VehicleSize.LARGE:
            self.large_available_inventory_space += quantity

    def decrement_available_space(self, vehicle_size, quantity):
        if vehicle_size == VehicleSize.SMALL:
            self.small_available_inventory_space -= quantity
        elif vehicle_size == VehicleSize.MEDIUM:
            self.medium_available_inventory_space -= quantity
        elif vehicle_size == VehicleSize.LARGE:
            self.large_available_inventory_space -= quantity

    def increment_inventory_quantity(self, inventory_item, quantity_to_add):
        check_if_space_available = self.check_if_enough_space_to_add_inventory(inventory_item.vehicle.size,
                                                                               quantity_to_add)
        if check_if_space_available:
            inventory_item.quantity_available += quantity_to_add
            self.decrement_available_space(inventory_item.vehicle.size, quantity_to_add)

    def decrement_inventory_quantity(self, inventory_item, quantity_to_remove):
        inventory_item.quantity_available -= quantity_to_remove
        self.increment_available_space(inventory_item.vehicle.size, quantity_to_remove)

    def add_inventory_item(self, vehicle, quantity_to_add):
        existing_item = self.check_if_exist(vehicle)
        if existing_item is not None:
            print('Inventory Item already exist')
            if self.check_if_enough_space_to_add_inventory(vehicle.size, quantity_to_add):
                self.increment_inventory_quantity(existing_item, quantity_to_add)
                print('Updated quantity in Inventory Catalog')
                return existing_item

        if self.check_if_enough_space_to_add_inventory(vehicle.size, quantity_to_add):
            inventory_item = InventoryItem(self.inventory_count_for_id, vehicle, vehicle.price, quantity_to_add)
            self.inventory_count_for_id += 1
            self.decrement_available_space(inventory_item.vehicle.size, quantity_to_add)
            self.inventory_list.add(inventory_item)
            print('Inventory Item added to Catalog')
            return inventory_item

        print('Not enough space to add Inventory')
        return existing_item

    def toString(self):
        inventory_catalog_string = ''
        for inventory_item in self.inventory_list:
            inventory_catalog_string = inventory_catalog_string + inventory_item.toString() + '\n'
        return inventory_catalog_string