# 6.Class Variables
# Problem: Add a class variable to car that keeps track of the number of cars created.

class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand          #private
        self.model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)                       
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"
    

my_tesla = ElectricCar("Tesla","Model S", "85kWh")
# print(my_tesla.brand)
# print(my_tesla.fuel_type())


safari = Car("Tata", "Safari")
safariThree = Car("Tata", "Nexon")
# print(safari.fuel_type())
print(safari.total_car)
test = Car("test", "test")
print(test.total_car)
print(Car.total_car)