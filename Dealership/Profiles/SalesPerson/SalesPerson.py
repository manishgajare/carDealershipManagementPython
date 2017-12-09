class SalesPerson:
    def __init__(self, id, person):
        self.__id = id
        self.__person = person

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
            return not self.__eq__(other)

    def __hash__(self):
        return hash(self.id)

    @property
    def id(self):
        return self.__id

    @property
    def person(self):
        return self.__person

    def toString(self):
        return 'id: {}, person: {}'.format(self.id, self.person)