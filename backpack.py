class Pack:
    def __init__(self, size, contents=[]):
        self.size = size
        self.contents = contents

    def addItem(self, item):
        current_size = 0
        for i in self.contents:
            current_size += i.size
        
        if current_size + item.size > self.size:
            print("Can't fit, too big")
            #real world, you would return this:
            #return False
        else:
            print(f"{item.__class__.__name__} added!")
            self.contents.append(item)
            #real world, you would return this:
            #return True

    def dropItem(self, item):
        if item in self.contents:
            print("Item removed from backpack")
            self.contents.remove(item)
        else:
            print("Item not in backpack")

    def packCapacity(self):
        current_size = 0
        for i in self.contents:
            current_size += i.size
        print(f"Backpack is {current_size} / {self.size}")
    
    def __str__(self):
        return ', '.join(self.contents)
        

class Item:

    def __init__(self, size):
        self.size = size

    def getSize(self):
        print(self.size)

    def __str__(self):
        return f"{self.__class__.__name__} item is {self.size} big"

class Potion(Item):
    
    def __init__(self, size, potency):
        super().__init__(size)
        self.potency = potency

    def use(self):
        print(self.potency)

class Weapon(Item):

    def __init__(self, size, power, range):
        self.size = size
        self.power = power
        self.range = range

    def getPower(self):
        print(self.power)

    def getRange(self):
        print(self.range)

class Axe(Weapon):

    def __init__(self, size, power, range, name):
        super().__init__(size, power, range)
        self.name = name

    def chop(self):
        print('chop')

    def swing(self):
        print('swing')

class Sword(Weapon):

    def __init__(self, size, power, range, name):
        super().__init__(size, power, range)
        self.name = name

    def thrust(self):
        print('thrust')

    def swing(self):
        print('swing')

my_pack = Pack(50)
my_sword = Sword(5, 10, 10, 'ten')
my_big_sword = Sword(55, 10, 10, 'ten')

my_pack.addItem(my_sword)
my_pack.packCapacity()
my_pack.dropItem(my_sword)
my_pack.packCapacity()
my_pack.addItem(my_big_sword)