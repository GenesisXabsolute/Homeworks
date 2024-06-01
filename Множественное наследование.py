class Vehicle:
    vehicle_type = "none"


class Car:
    price = 1000000

    def horse_power(self):
        #        return quantity
        pass


class Nissan(Car, Vehicle):
    price = 2300000
    vehicle_type = "4 wheels"

    def horse_power(self):
        super().horse_power()


n = Nissan()
print(n.vehicle_type)
print(n.price)
