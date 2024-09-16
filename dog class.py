#Dog is a Class - Object
class Dog:

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
        
    def speak(self):
        if self.breed == "Rotty":
            return 'Bork'
        return 'Woof'

    def __str__(self):
        return f'{self.name} is a {self.age} year old {self.breed}'
    
#Line 14 instantiates line 2
#dog is a Variable - Instance of an object
dog = Dog('Whatabout', 5, 'Rotty')
dog2 = Dog('Obb', 23, 'red')
 
dog3 = Dog('bob', 1, 'kelpie')
dog4 = Dog('bob', 1, 'kelpie')