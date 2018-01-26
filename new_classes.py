'''
Inheritance demonstration
'''
class Vehicle(object):
    # Sets up our parent class of Vehicle that subclasses can inherit from
    def __init__(self, wheels, capacity, make, model):
        self.wheels = wheels
        self.capacity = capacity
        self.make = make
        self.model = model
        self.mileage = 0
    def drive(self, miles):
        self.mileage += miles
        return self
    def reverse(self, miles):
        self.mileage -= miles
        return self
class Bike(Vehicle):
    # the vehicle class Bike inherits from the parent class Vehicle, denoted by Vehicle enclosed in parens
    def vehicle_type(self):
        # Simply sets what type of vehicle the class is
        return 'Bike'
class Car(Vehicle):
    def set_wheels(self):
        self.wheels = 4
        return self
class Airplane(Vehicle):
    def fly(self, miles):
        self.mileage += miles
        return self
v = Vehicle(4,8,'Dodge', 'minivan')
print v.make
b = Bike(2, 1, 'Schwinn', 'Paramount')
# When we use these parameters for our new Bike, it fills -  from top to bottom - the information
# set up in our Vehicle parent class... Wheels, Seating capacity, make, model and mileage
print b.vehicle_type()
c = Car(8, 5, 'Toyota', 'Tacoma')
c.set_wheels()
print c.wheels
a = Airplane(22, 853, 'Airbus', 'A380')
a.fly(580)
print a.mileage

'''
When we defined each of our classes, we typed Bike(Vehicle), Car(Vehicle), and Airplane(Vehicle).
You could read each of these like "Make a class Bike/Car/Airplane that inherits from Vehicle".
This is what is known as the implicit inheritance which allows us to use inherited attributes
and methods of the Vehicle(parent) class in our new subclasses.

A general skeleton for implicit inheritance:
'''
# class Parent(object): # inherits from the object class
#   # parent methods and attributes here
# class Child(Parent): #inherits from Parent class so we define Parent as the first parameter
#   # parent methods and attributes are implicitly inherited
#   # child methods and attributes
