from Dealership.Inventory.VehicleFeatures.VehicleSize import VehicleSize
from Dealership.Inventory.InventoryItem import InventoryItem
import threading


class InventoryCatalog:
    __SMALL_TOTAL_INVENTORY_SPACE = 180
    __MEDIUM_TOTAL_INVENTORY_SPACE = 170
    __LARGE_TOTAL_INVENTORY_SPACE = 150

    __small_available_inventory_space = __SMALL_TOTAL_INVENTORY_SPACE
    __medium_available_inventory_space = __MEDIUM_TOTAL_INVENTORY_SPACE
    __large_available_inventory_space = __LARGE_TOTAL_INVENTORY_SPACE

    __instance = None
    __lock = threading.Lock()
    __inventory_list = None
    __inventory_count_for_id = None

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
        self.__inventory_list = set()
        self.__inventory_count_for_id = 1
        self.__initialized = True

    def get_inventory_list(self):
        return self.__inventory_list

    def get_small_available_inventory_space(self):
        return self.__small_available_inventory_space

    def get_medium_available_inventory_space(self):
        return self.__medium_available_inventory_space

    def get_large_available_inventory_space(self):
        return self.__large_available_inventory_space

    def get_small_total_inventory_space(self):
        return self.__SMALL_TOTAL_INVENTORY_SPACE

    def get_medium_total_inventory_space(self):
        return self.__MEDIUM_TOTAL_INVENTORY_SPACE

    def get_larger_total_inventory_space(self):
        return self.__LARGE_TOTAL_INVENTORY_SPACE

    def remove_inventory_item(self, inventory_item, quantity):
        self._decrement_inventory_quantity(inventory_item, quantity)

    def check_if_exist(self, vehicle):
        for item in self.__inventory_list:
            if item.vehicle == vehicle:
                return item
        return None

    def check_if_enough_space_to_add_inventory(self, vehicle_size, quantity_to_add):
        is_available = False
        if ((vehicle_size == VehicleSize.SMALL and quantity_to_add <= self.__small_available_inventory_space) or
                (vehicle_size == VehicleSize.MEDIUM and quantity_to_add <= self.__medium_available_inventory_space) or
                (vehicle_size == VehicleSize.LARGE and quantity_to_add <= self.__large_available_inventory_space)):
            is_available = True
        return is_available

    def _increment_available_space(self, vehicle_size, quantity):
        if vehicle_size == VehicleSize.SMALL:
            self.__small_available_inventory_space += quantity
        elif vehicle_size == VehicleSize.MEDIUM:
            self.__medium_available_inventory_space += quantity
        elif vehicle_size == VehicleSize.LARGE:
            self.__large_available_inventory_space += quantity

    def _decrement_available_space(self, vehicle_size, quantity):
        if vehicle_size == VehicleSize.SMALL:
            self.__small_available_inventory_space -= quantity
        elif vehicle_size == VehicleSize.MEDIUM:
            self.__medium_available_inventory_space -= quantity
        elif vehicle_size == VehicleSize.LARGE:
            self.__large_available_inventory_space -= quantity

    def _increment_inventory_quantity(self, inventory_item, quantity_to_add):
        check_if_space_available = self.check_if_enough_space_to_add_inventory(inventory_item.vehicle.size,
                                                                               quantity_to_add)
        if check_if_space_available:
            inventory_item.quantity_available += quantity_to_add
            self._decrement_available_space(inventory_item.vehicle.size, quantity_to_add)

    def _decrement_inventory_quantity(self, inventory_item, quantity_to_remove):
        inventory_item.quantity_available -= quantity_to_remove
        self._increment_available_space(inventory_item.vehicle.size, quantity_to_remove)

    def add_inventory_item(self, vehicle, quantity_to_add):
        existing_item = self.check_if_exist(vehicle)
        if existing_item is not None:
            print('Inventory Item already exist')
            if self.check_if_enough_space_to_add_inventory(vehicle.size, quantity_to_add):
                self._increment_inventory_quantity(existing_item, quantity_to_add)
                print('Updated quantity in Inventory Catalog')
                return existing_item

        if self.check_if_enough_space_to_add_inventory(vehicle.size, quantity_to_add):
            inventory_item = InventoryItem(self.__inventory_count_for_id, vehicle, vehicle.price, quantity_to_add)
            self.__inventory_count_for_id += 1
            self._decrement_available_space(inventory_item.vehicle.size, quantity_to_add)
            self.__inventory_list.add(inventory_item)
            print('Inventory Item added to Catalog')
            return inventory_item

        print('Not enough space to add Inventory')
        return existing_item

    def toString(self):
        inventory_catalog_string = ''
        for inventory_item in self.__inventory_list:
            inventory_catalog_string = inventory_catalog_string + inventory_item.toString() + '\n'
        return inventory_catalog_string