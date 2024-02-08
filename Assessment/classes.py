class Vehicle:
    def __init__(self, vehicle_id, fare_per_km):
        self.vehicle_id = vehicle_id
        self.fare_per_km = fare_per_km

    # Question 1: Return a string representation of the object
    # Your code here


    # Question 2: Get the fare per km for the vehicle. How can we make this a property instead of a method?
    def get_fare_per_km(self):
        pass    # Your code here


class Trip:
    def __init__(self, cab_driver, start_location, end_location, distance, vehicle):
        self.cab_driver = cab_driver
        self.start_location = start_location
        self.end_location = end_location
        self.distance = distance
        self.vehicle = vehicle

    def calculate_fare(self):
        # Calculate the fare for the trip by using distance and fare.
        pass  # Your code here

    def change_end_location():
        # Change the end location of the trip
        pass  # Your code here

    # Implement operator overloading here for the following comparisons:
    # 1. Greater than (>)
    # 2. Less than (<)
    # 3. Equal to (==)

    def __gt__(self, other):
        pass  # Your code here for greater than

    def __lt__(self, other):
        pass  # Your code here for less than

    def __eq__(self, other):
        pass  # Your code here for equal to

# <---------------Inherit from the Vehicle class---------------->

# We want a new class called ElectricVehicle that inherits from the Vehicle class.
# The ElectricVehicle class should have an additional attribute called battery_capacity.

class ElectricVehicle():
    pass    # Your code here

