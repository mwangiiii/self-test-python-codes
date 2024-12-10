# Base Class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")

# Derived Class for Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Derived Class for Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Derived Class for Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Derived Class for Bicycle
class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚴")

# Create objects for each vehicle
car = Car()
plane = Plane()
boat = Boat()
bicycle = Bicycle()

# Demonstrate polymorphism
vehicles = [car, plane, boat, bicycle]
for vehicle in vehicles:
    vehicle.move()
