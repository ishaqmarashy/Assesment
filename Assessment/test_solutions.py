from classes import Vehicle, Trip, ElectricVehicle

"""Dont edit this file"""

if __name__ == "__main__":
    # Test the vehicle class
    vehicle1 = Vehicle(vehicle_id="V1", fare_per_km=10.0)
    vehicle2 = Vehicle(vehicle_id="V2", fare_per_km=12.0)

    # Test the trip class
    trip1 = Trip(cab_driver="D1", start_location="A", end_location="B", distance=10, vehicle=vehicle1)
    trip2 = Trip(cab_driver="D2", start_location="A", end_location="B", distance=15, vehicle=vehicle2)

    # Test the methods on the vehicle class
    print("The fare for trip1 is:", vehicle1.get_fare_per_km)

    # Test the methods on the trip class
    trip1.change_end_location("C")
    print("The new end location for trip1 is:", trip1.end_location)

    # Test the methods on the trip class
    print("The fare for trip1 is:", trip1.calculate_fare())

    # Test the comparisons
    print("Is trip1 greater than trip2?", trip1 > trip2)
    print("Is trip1 less than trip2?", trip1 < trip2)
    print("Are trip1 and trip2 equal?", trip1 == trip2)

    # Test the ElectricVehicle class
    electric_vehicle = ElectricVehicle(vehicle_id="V3", fare_per_km=15.0, battery_capacity=100)
    print(electric_vehicle)
    print(electric_vehicle.battery_capacity)