class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor
    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floor:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)

h1 = House('house', 30)
h1.go_to(45)