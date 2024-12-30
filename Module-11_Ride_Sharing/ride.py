from datetime import datetime
from vehicle import Car, Bike


class RideSharing:
    def __init__(self, company_name):
        self.company_name = company_name
        self.riders = []
        self.drivers = []
        self.rides = []

    def add_rider(self, rider):
        self.riders.append(rider)

    def add_driver(self, driver):
        self.drivers.append(driver)

    def __str__(self):
        return f"Company Name: {self.company_name} with riders : {len(self.riders)} and Drivers: {len(self.drivers)}"


class Ride:

    def __init__(self, start_location, end_location, vehicle):
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = None
        self.vehicle = vehicle

    def set_driver(self, driver):
        self.driver = driver

    def start_ride(self, distance):
        self.start_time = datetime.now()
        self.estimated_fare = self.calculate_fare(distance, self.vehicle.vehicle_type)
        print(
            f"The ride from {self.start_location} to {self.end_location} has started at {self.start_time}. "
            f"Estimated fare: {self.estimated_fare}"
        )

    def end_ride(self):
        if self.driver is None or self.rider is None:
            print("Ride has not started properly. Missing rider or driver.")
            return

        print(f"Ending ride with fare: {self.estimated_fare}")
        print(f"Rider's wallet before: {self.rider.wallet}")
        print(f"Driver's wallet before: {self.driver.wallet}")

        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare

        print(f"Rider's wallet after: {self.rider.wallet}")
        print(f"Driver's wallet after: {self.driver.wallet}")

    def calculate_fare(self, distance, vehicle):
        fare_per_km = {"car": 30, "bike": 20, "cng": 25}
        return distance * fare_per_km[vehicle]

    def __repr__(self):
        return f"Ride details: {self.start_location} to {self.end_location} "


class RideRequest:

    def __init__(self, rider, end_location):
        self.rider = rider
        self.end_location = end_location


class RideMatching:

    def __init__(self, drivers):
        self.available_drivers = drivers

    def find_drivers(self, ride_request, vehicle_type, distance):
        if len(self.available_drivers) > 0:
            print("Looking for drivers . . . .")
            driver = self.available_drivers[0]

            if vehicle_type == "car":
                vehicle = Car("car", "ABC-123", 30)
            elif vehicle_type == "bike":
                vehicle = Bike("bike", "XY-521", 20)

            # Create a Ride and set both rider and driver
            ride = Ride(
                ride_request.rider.current_location, ride_request.end_location, vehicle
            )
            ride.rider = ride_request.rider  # Set the rider
            driver.accept_ride(ride, distance)
            return ride
