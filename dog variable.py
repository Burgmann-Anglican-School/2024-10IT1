#Creating a dog using variables
dog_name = input("Enter name: ")
dog_age = int(input("Enter age: "))
dog_breed = input("Enter breed: ")
#Loading those variables into a dictionary
dog = {'name': dog_name, 'age':dog_age,'breed':dog_breed}
#Printing the dog
print(f'{dog["name"]} is a {dog["breed"]} that is {dog["age"]} years old.')