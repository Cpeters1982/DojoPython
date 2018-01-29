class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health = self.health-1
        return self
    def run(self):
        self.health = self.health-5
        return self
    def display_health(self, name):
        print 'The animal is named {} and has {} health'.format(name, self.health)
        return self
class Dog(Animal):
    def __init__(self):
        super(Dog, self).__init__(Dog, self)
        self.health = 150
    def pet(self):
        self.health += 5
        return self
class Dragon(Animal):
    def __init__(self):
        super(Dragon, self).__init__(Dragon, self)
        self.health = 170
        print 'I am a dragon'
    def fly(self):
        self.health -= 10
        return self

# a = Animal('Shithead', 50)
# print a.walk().walk().walk().run().run().display_health()
d = Dog()
print d.walk().walk().walk().run().run().pet().display_health(name = 'Bagel')
drago = Dragon()
print drago.fly().display_health(name = 'Drago')
