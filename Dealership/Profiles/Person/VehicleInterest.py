class VehicleInterest:
    def __init__(self):
        self.__vehicle_list = set()

    def __str__(self):
        vehicle_list_string = 'Vehicle List -> '
        for vehicle in self.__vehicle_list:
            vehicle_list_string = vehicle_list_string + vehicle.__str__() + '\n'
        return vehicle_list_string

    @property
    def vehicle_list(self):
        return self.__vehicle_list

    @vehicle_list.setter
    def vehicle_list(self, vehicle_list):
        self.__vehicle_list = vehicle_list


