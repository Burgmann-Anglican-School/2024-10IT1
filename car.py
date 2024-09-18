class Car:
    def __init__(self, colour, ks):
        #Attribute or property
        self.colour = colour
        self.ks = ks
    #Methods
    def __str__(self):
        return f'The {self.colour} car has {self.ks} kilometres.'
    # by not using underscores we have made a new method that doesn't work when you use 'print'
    #   but can be called like it is on line 14
    def str(self):
        return f'The {self.colour} car has {self.ks} kilometres.'
    def speed(self, spd):
        return f'You are going {spd}'

class Merc(Car):
    def speed(self, spd='fast'):
        return super().speed(spd)

class Audi(Car):
    pass

car1 = Car('red', 30000)
car2 = Merc('blue', 20000)
print(car2)
print(car2.str())
print(car1)
print(car2.speed())