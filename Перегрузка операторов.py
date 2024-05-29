class Building:
    def __init__(self, number_of_floor, building_type):
        self.number_of_floor = number_of_floor
        self.building_type = building_type

    def __eq__(self, other):
        a = self.number_of_floor == other.number_of_floor
        b = self.building_type == other.building_type
        return a, b


a = Building(3, 'qwerty')
b = Building(5, 'asdfgh')

print(a.__eq__(b))

