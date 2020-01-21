# Move all common properties in your vehicles to a new Vehicle class.

class Vehicle:
    def __init__(self):
        self.name = "car"
        self.color = "red"
        self.torque = "quite torquey"
        self.cool_factor = "fairly cool"

# Create a drive() method in the Vehicle class.

    def drive(self):
        print(f"I'm a {self.color} {self.name}.")

# Create a turn(self, direction) method, and a stop(self) method on Vehicle. Define a basic implementation of each.

    def turn(self, direction):
        print(f"The {self.name} is turning {direction}")

    def stop(self):
        print(f"The {self.name} comes to a stop.")

# Define 5 of your favorite vehicles

# Override the drive() method in all the other vehicle classes. Include the vehicle's color in the message (i.e. "The blue Ram drives past. RRrrrrrummbbble!").

# Override all three of those methods on some of the vehicles. For example, the stop() method for a plane would be to output the message "The white Cessna rolls to a stop after rolling a mile down the runway."

class Prius(Vehicle):
    def __init__(self):
        super().__init__()
        self.gas_milage = 50
        self.make = "Toyota"
        self.price = 20000

    def drive(self):
        print(f"The {self.color} {self.name} drives. Crickets.")
    
    def turn(self, direction):
        print(f"The {self.name} is veering {direction}")

class Spyder(Vehicle):
    def __init__(self):
        super().__init__()
        self.gas_mileage = 20
        self.type = "convertable"
        self.make = "Toyota"
        self.price = 30000

    def drive(self):
        print(f"The {self.color} {self.name} races by. ZOOM!")

class Ferrari(Vehicle):
    def __init__(self):
        super().__init__()
        self.gas_mileage = 19
        self.type = "convertable" 
        self.price = 50000
        self.make = "Ferrari"

    def drive(self):
        print(f"I'm a {self.color} {self.name} and I go FAST. ZIP!")

class Leaf(Vehicle):
    def __init__(self, type):
        super().__init__()
        self.price = 20000
        self.make = "Nissan"

    def drive(self):
        print(f"The {self.color} {self.name} quietly drives down the street.")


class FlyingCar(Vehicle):
    def __init__(self):
        super().__init__()
        self.lift = "2000ft"
    
    def drive(self):
        print(f"The {self.color} {self.name} is smooth and quiet as it flies.")

    def turn(self, direction):
        print(f"The {self.name} changes course, veering off the the {direction}.")

# Create an instance of each vehicle.
jetson = FlyingCar()
bessie = Prius()
autumn = Leaf("electric")
crawly = Spyder()
fiddler = Ferrari()


# Define a different value for each vehicle's properties.
# flying car
jetson.name = "flying car"
jetson.torque = "mega torquoise"
jetson.color = "opalescent"
jetson.cool_factor = "highly cool"
# prius
bessie.name = "prius"
bessie.torque = "not very torquey"
bessie.color = "blue"
bessie.cool_factor = "pretty cool"
# leaf
autumn.name = "leaf"
autumn.torque = "not amazing"
autumn.color = "white lightning" 
autumn.cool_factor = "kinda cool"
#  spyder
crawly.name = "spyder" 
#  ferarri
fiddler.name = "ferarri"



# Make your vehicle instances perform all three behaviors. 

bessie.drive()
bessie.turn("right")
bessie.stop()
bessie.turn("right")

crawly.drive()
crawly.turn("left")
crawly.stop()

fiddler.drive()
fiddler.turn("left")
fiddler.stop()

autumn.drive()
autumn.turn("left")
autumn.stop()

jetson.drive()
jetson.turn("left")
jetson.stop()