class User(object):
    '''Make a class of User that contains the following attributes and methods'''
    def __init__(self, name,email):
        '''Sets the User-class attributes; name, email and whether the user is logged in or not (defaults to true)'''
        self.name = name
        self.email = email
        self.logged = True
    def login(self):
        '''Creates a Login method for the User-class. This method logs the user in'''
        self.logged = True
        print self.name + " is logged in."
        return self
    def logout(self):
        '''Creates a Logout method for the User-class. This method logs the user out.'''
        self.logged = False
        print self.name + " is not logged in."
        return self
    def show(self):
        '''Creates a Show method for the User-class. Displays the users' name and email'''
        print "My name is {}. You can email me at {}".format(self.name, self.email)
        return self

new_user = User("Chris", "chris@chris.com")
'''Instantiates a new instance of the User_class with the name and email attributes assigned to "chris" and "chris@chris.com" respectively'''
print "Hello, my name is " + new_user.name, "and my email address is " + new_user.email

'''
Remember, objects have two important features: storage of information and ability to execute some
logic.

To review:

A class: Instructions on how to build many objects that share characteristics.
An object: A data type built according to specifications provided by the class definition.
An attribute: A value. Think of an attribute as a variable that is stored within an object.
A method: A set of instructions. Methods are functions that are associated with an object.
Any function included in the parent class definition can be called by an object of that class.
'''
