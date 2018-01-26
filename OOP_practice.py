# # pylint: disable=invalid-name
# class User(object):
#     '''Make a class of User that contains the following attributes and methods'''
#     def __init__(self, name, email):
#         '''Sets the User-class attributes; name, email and whether the user is logged in or not (defaults to true)'''
#         self.name = name
#         self.email = email
#         self.logged = True
#     # Login method changes the logged status for a single instance (the instance calling the method)
#     def login(self):
#         '''Creates a Login method for the User-class. This method logs the user in'''
#         self.logged = True
#         print self.name + " is logged in."
#         return self
#     # logout method changes the logged status for a single instance (the instance calling the method)
#     def logout(self):
#         '''Creates a Logout method for the User-class. This method logs the user out.'''
#         self.logged = False
#         print self.name + " is not logged in."
#         return self
#     def show(self):
#         '''Creates a Show method for the User-class. Prints the users' name and email'''
#         print "My name is {}. You can email me at {}".format(self.name, self.email)
#         return self

# new_user = User("Chris", "chris@chris.com")

'''
Instantiates a new instance of the User_class with the name and email attributes assigned to "chris" and "chris@chris.com" respectively
'''
# print "Hello, my name is " + new_user.name, "and my email address is " + new_user.email

'''
Remember, objects have two important features: storage of information and ability to execute some
logic.

To review:

A class: Instructions on how to build many objects that share characteristics.
An object: A data type built according to specifications provided by the class definition.
An attribute: A value. Think of an attribute as a variable that is stored within an object.
A method: A set of instructions. Methods are functions that are associated with an object.
Any function included in the parent class definition can be called by an object of that class.

 
1. If we wanted to define a new class we would start with which line

 def ClassName(object):
 def ClassName(self):
 class ClassName(self):
 [x] class ClassName(object):
 None of the above
 
2. How can we set attributes to an instance of a class

 A. Initializing our attributes with the __init__() function
 B. We create attributes by defining multiple setter methods in our class
 C. This is impossible
 D. We can set individual attributes to each instance - one by one
 [x] Both A & D
 
3. The __init__() function gets called while the object is being constructed

 True
 [x] False
 
4. You cannot define an __init__() function that has parameters

 True
 [x] False
 
5. How do you pass arguments to the __init__() function?

 Creating an object instance and calling the __init__() function on the object passing in the specified parameters
 You cannot pass arguments into a __init__() function
 [x] When creating an object instance you pass the arguments to the specified class you are creating an instance of
 Creating an object within the class and calling the __init__() function passing the specified parameters
 
6. What is the purpose of an __init__() function?

 To prevent you from rewriting the same code each time you create a new object
 To set properties required to execute certain instance methods as soon as the object is instantiated
 To execute whatever logic we want to for each object that is created
 [x] All of the above
 
7. A constructor function cannot call any other methods inside the class.

 True
 [x] False
'''


# class Bike(object):
#     '''
#     Bike class!
#     '''
#     def __init__(self, price, max_speed, miles):
#         self.price = price
#         self.max_speed = max_speed
#         self.miles = 0
#     def displayinfo(self):
#         '''
#         Get that info, son!
#         '''
#         print "This bike costs ${}. It has a max speed of {}. It has been ridden {} miles.".format(self.price, self.max_speed, self.miles)
#         return self
#     def ride(self):
#         '''
#         Ride that bike!
#         '''
#         print "Riding "
#         self.miles = self.miles+10
#         return self
#     def reverse(self):
#         '''
#         Better backpedal...
#         '''
#         self.miles = self.miles-5 if self.miles-5 > 0 else 0
#         return self

# bike1 = Bike(200, 10, 0)
# bike2 = Bike(300, 20, 0)
# bike3 = Bike(600, 60, 0)
# bike1.ride().ride().ride().reverse().displayinfo()
# bike2.ride().ride().reverse().reverse().displayinfo()
# bike3.reverse().reverse().reverse().displayinfo()


# class Car(object):
#     def __init__(self, price, speed, fuel, mileage):
#         self.price = price
#         self.speed = speed
#         self.fuel = fuel
#         self.mileage = mileage
#         if self.price > 10000:
#             self.tax = 0.15
#         else:
#             self.tax = 0.12
#         self.display_all()
#     def display_all(self):
#         print 'Price: ' + str(self.price)
#         print 'Speed: ' + self.speed
#         print 'Fuel: ' + self.fuel
#         print 'Mileage: ' + self.mileage
#         print 'Tax: ' + str(self.tax)
#         return self

# car1 = Car(20000, '100mph', 'Full', '30mpg')
# car2 = Car(1000, '45mph', 'Not full', '15mpg')
# car3 = Car(10000, '75mph', 'Full', '32mpg')

