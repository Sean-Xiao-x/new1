
# class Dog():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def sit(self):
#         print(self.name.title() + " is now sitting.")
#     def roll_over(self):
#         print(self.name.title() + " rolled over!")
# my_dog = Dog('willie', 6)
# print("My dog's name is " + my_dog.name.title() + ".")
# print("My dog is " + str(my_dog.age) + " years old.")
# my_dog.sit()
# my_dog.roll_over()

# class Car():
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())

# class Car():
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#     def read_odometer(self):
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

