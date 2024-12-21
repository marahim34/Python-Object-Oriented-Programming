class Company:
    def __init__(self, name, address, ) -> None:
        self.name = name
        self.bus = []
        self.routes = []
        self.count = []
        self.manager = []
        self.supervisor = []
        self.fare = []
        self.address = address

class Driver:
    def __init__(self, name, license, age):
        self.name = name
        self.license = license
        self.age = age

class Counter:
    def __init__(self):
        pass

    def purchase_a_ticket(self, start, destination, airConditioned, normal):
        pass


class Passenger:
    def __init__(self):
        pass