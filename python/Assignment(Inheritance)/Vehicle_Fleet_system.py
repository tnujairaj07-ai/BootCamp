class Vehicle:
    total_vehicles = 0

    def __init__(self, name):
        self.name = name
        Vehicle.total_vehicles += 1
    def fuel_cost(self, km):
        return 0

class Car(Vehicle):
    def __init__(self, name):
        super().__init__(name)
    def fuel_cost(self, km):
        return km * 8

class Truck(Vehicle):
    def __init__(self, name):
        super().__init__(name)
    def fuel_cost(self, km):
        return km * 15

class Motorcycle(Vehicle):
    def __init__(self, name):
        super().__init__(name)

    def fuel_cost(self, km):
        return km * 3

class ElectricCar(Car):
    def __init__(self, name):
        super().__init__(name)
    def fuel_cost(self, km):
        return 0
    
def fleet_report(vehicle_list, km):
    print("----- Fleet Report -----")
    for vehicle in vehicle_list:

        print("Vehicle :", vehicle.name)
        print("Type    :", vehicle.__class__.__name__)
        print("Cost for", km, "km =", vehicle.fuel_cost(km))
        if isinstance(vehicle, ElectricCar):
            print("This is an Electric Car.")

        print()

v1 = Car("Maruti Swift")
v2 = Truck("Tata Truck")
v3 = Motorcycle("Hero Splendor")
v4 = ElectricCar("Tata Nexon EV")

fleet = [v1, v2, v3, v4]
fleet_report(fleet, 100)
print("Total Vehicles Created:", Vehicle.total_vehicles)