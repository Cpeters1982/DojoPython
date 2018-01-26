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
    def display_health(self):
        print 'the animal has {} health'.format(self.health)
        return self
class Dog(Animal):
    def set_health(self):
        self.health = 150
        return self
    def pet(self):
        self.health = self.health+5
        return self

# a = Animal('Shithead', 50)
# print a.walk().walk().walk().run().run().display_health()
d = Dog('Bagel', 150)
print d.walk().walk().walk().run().run().pet().display_health()
