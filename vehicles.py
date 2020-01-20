# Move all common properties in your vehicles to a new Vehicle class.

class Vehicle:
    def __init__(self):
        self.name = "car"
        self.color = "red"
        self.torque = "quite torquey"
        self.cool_factor = "fairly cool"

# Create a drive() method in the Vehicle class.

    def drive(self):
        print("Weeeee! On the road again.")

# Define 5 of your favorite vehicles
class Prius(Vehicle):
    def __init__(self):
        super().__init__()
        self.gas_milage = 50
        self.make = "Toyota"
        self.price = 20000

    def drive(self):
        print(f"I'm a {self.name}. Look at me go!")

class Spyder(Vehicle):
    def __init__(self):
        super().__init__()
        self.gas_mileage = 20
        self.type = "convertable"
        self.make = "Toyota"
        self.price = 30000

    def drive(self):
        print(f"I'm a {self.name}. Look at me go!")

class Ferrari(Vehicle):
    def __init__(self):
        super().__init__()
        self.gas_mileage = 19
        self.type = "convertable"
        self.price = 50000
        self.make = "Ferrari"

class Leaf(Vehicle):
    def __init__(self):
        super().__init__()
        self.price = 20000
        self.make = "Nissan"

class FlyingCar(Vehicle):
    def __init__(self):
        super().__init__()
        self.lift = "2000ft"

# Create an instance of each vehicle.
jetson = FlyingCar()
bessie = Prius()
autumn = Leaf()
crawly = Spyder()
fiddler = Ferrari()


# Define a different value for each vehicle's properties.
jetson.torque = "mega torquoise"
jetson.color = "opalescent"
jetson.cool_factor = "highly cool"
print(jetson.torque, jetson.color, jetson.cool_factor, jetson.lift) 
bessie.torque = "not very torquey"
bessie.color = "blue"
bessie.cool_factor = "pretty cool"
print(bessie.torque, bessie.color, bessie.cool_factor, bessie.make, bessie.price)
autumn.torque = "not amazing"
autumn.color = "white lightning" 
autumn.cool_factor = "kinda cool"
print(autumn.torque, autumn.color, autumn.cool_factor, autumn.make, autumn.price) 
print(crawly.torque, crawly.color, crawly.cool_factor, crawly.make, crawly.price, crawly.type) 
print(fiddler.torque, fiddler.color, fiddler.cool_factor, fiddler.make, fiddler.price, fiddler.type) 


# Override the drive() method in all the other vehicle classes. Include the vehicle's color in the message (i.e. "The blue Ram drives past. RRrrrrrummbbble!").


# Create a turn(self, direction) method, and a stop(self) method on Vehicle. Define a basic implementation of each.


# Override all three of those methods on some of the vehicles. For example, the stop() method for a plane would be to output the message "The white Cessna rolls to a stop after rolling a mile down the runway."


# Make your vehicle instances perform all three behaviors. 