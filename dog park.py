class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age} years old'
    
    def speak(self, words):
        return f'{self.name} says {words}'

#This class is a child class of the Dog class.
class Dachsund(Dog):
    
    def speak(self):
        return f'{self.name} says "oof"'

class Lab(Dog):
    # this is bad programming, you should just write pass
    def speak(self, words):
        return super().speak(words)

class Corgi(Dog):
    def speak(self):
        return f'{self.name} says "yap"'
    
class GoldenRetriever(Dog):
    def speak(self, words='bark'):
        return super().speak(words)

dog1 = Dog('Sir Jeffington III', 3)
dog2 = Dachsund('Sausage', 1)
dog3 = Lab('Ted', 5)
dog4 = Corgi('George', 4)
print('Here are all the dogs:')
print(dog1)
print(dog2)
print(dog3)
print(dog4)

print('Here is what they say:')
print(dog1.speak('woof'))
print(dog2.speak())
print(dog3.speak('hello'))
print(dog4.speak())
