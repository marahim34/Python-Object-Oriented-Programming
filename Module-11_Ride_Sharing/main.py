from ride import Ride, RideRequest, RideMatching, RideSharing
from users import Rider, Driver
from vehicle import Car, Bike

uber_ride = RideSharing("UBER Ride")
joe = Rider("Joe Biden", "joe@gmail.com", 12345687, "Washington DC", 5)
uber_ride.add_rider(joe)

donald = Driver("Donald Trump", "donald@gmail.com", 12545687, "Philadelphia")
uber_ride.add_driver(donald)

print(uber_ride)
