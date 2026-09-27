# class Car:
#     brand = None
#     model = None
# my_car = Car()
# print(my_car)

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

# my_car = Car("Toyota", "corolla")
# print(my_car.brand)
# print(my_car.model)


class Car:
    class_count = 0
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.class_count +=1

    def fullName(self):
        return f"{self.brand} {self.model}"
    def fuel_type(self):
        return "Petrol or Diesel"
    def add(self, a = 0, b = 0, c = 0):
        return a+b+c

my_car = Car("Toyota", "corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.fullName())

class ElectricCar(Car):
    def __init__(self, brand, model,batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize
    def fuel_type(self):
        return "Electric Charge"

my_another_car = ElectricCar("Telsa","Model-Y", "85kwh")
# print(my_another_car.brand)
# print(my_another_car.model)
# print(my_another_car.batterySize)
# print(my_another_car.fullName())

print(my_car.fuel_type())
print(my_another_car.fuel_type())
print(my_car.add(5, 10))
print(my_car.class_count)