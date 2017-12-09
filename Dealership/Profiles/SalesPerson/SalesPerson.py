class SalesPerson:
    __id = 0
    __person = None

    def __init__(self, id, person):
        self.__id = id
        self.__person = person

    def __eq__(self, other):
        return self.get_id() == other.get_id()

    def __ne__(self, other):
            return not self.__eq__(other)

    def __hash__(self):
        return hash(self.__id)

    def get_id(self):
        return self.__id

    def get_person(self):
        return self.__person

    def toString(self):
        return 'id: {}, person: {}'.format(self.__id, self.__person)