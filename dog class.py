#Dog is a Class - Object
class Dog:

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
        
    def __str__(self):
        return f'{self.name} is a {self.age} year old {self.breed}'
    
#Line 14 instantiates line 2
#dog is a Variable - Instance of an object
dog = Dog(input('Name: '), int(input('Age: ')), input('Breed: '))
dog2 = Dog('bob',23,'red')
print(dog.name)
print(dog)