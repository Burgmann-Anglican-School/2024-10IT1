dog_name = input("Enter name: ")
dog_age = int(input("Enter age: "))
dog_breed = input("Enter breed: ")
dog = {'name': dog_name, 'age':dog_age,'breed':dog_breed}
print(f'{dog_name} is a {dog_breed} that is {dog_age} years old.')