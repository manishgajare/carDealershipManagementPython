class VehicleInterest:
    __vehicle_list = None

    def __init__(self):
        self.__vehicle_list = set()

    def get_vehicle_list(self):
        return self.__vehicle_list

    def set_vehicle_list(self, vehicle_list):
        self.__vehicle_list = vehicle_list

    def toString(self):
        vehicle_list_string = ''
        print('Vehicle List -> ')
        for vehicle in self.__vehicle_list:
            vehicle_list_string = vehicle_list_string + vehicle.toString() + '\n'
        return vehicle_list_string

