from ride import Ride, RideRequest, RideMatching, RideSharing
from users import Rider, Driver
from vehicle import Car, Bike

uber_ride = RideSharing("UBER Ride")
joe = Rider("Joe Biden", "joe@gmail.com", 12345687, "Washington DC", 50)
uber_ride.add_rider(joe)

donald = Driver("Donald Trump", "donald@gmail.com", 12545687, "Philadelphia")
uber_ride.add_driver(donald)

distance = 15
joe.request_ride(uber_ride, "California", "car", distance)
joe.show_current_ride()
donald.reach_destination(joe.current_ride)

print(f"Joe's wallet after ride: ${joe.wallet}")
print(f"Donald's wallet after ride: ${donald.wallet}")
print(uber_ride)
