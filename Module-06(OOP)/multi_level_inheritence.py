# Base class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"Vehicle: {self.brand} {self.model}"


# Intermediate class
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)  # Call the base class constructor
        self.doors = doors

    def car_info(self):
        return f"Car: {self.brand} {self.model}, Doors: {self.doors}"


# Derived class
class ElectricCar(Car):
    def __init__(self, brand, model, doors, battery_capacity):
        super().__init__(brand, model, doors)  # Call the intermediate class constructor
        self.battery_capacity = battery_capacity

    def electric_car_info(self):
        return f"Electric Car: {self.brand} {self.model}, Doors: {self.doors}, Battery: {self.battery_capacity} kWh"


# Using the classes
vehicle = Vehicle("Generic", "Model X")
print(vehicle.info())

car = Car("Toyota", "Camry", 4)
print(car.car_info())

electric_car = ElectricCar("Tesla", "Model 3", 4, 75)
print(electric_car.electric_car_info())
