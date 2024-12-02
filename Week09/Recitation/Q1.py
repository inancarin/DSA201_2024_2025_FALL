# Vehicle class
class Vehicle:
    def __init__(self, color, tireNumber):
        self._color = color
        self._tireNumber = tireNumber

    # Getter and Setter for color
    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    # Getter and Setter for tireNumber
    def get_tireNumber(self):
        return self._tireNumber

    def set_tireNumber(self, tireNumber):
        self._tireNumber = tireNumber


# Car class inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, color, tireNumber, brand, km, constructionYear):
        super().__init__(color, tireNumber)
        self._brand = brand
        self._km = km
        self._constructionYear = constructionYear

    # Getter and Setter for brand
    def get_brand(self):
        return self._brand

    def set_brand(self, brand):
        self._brand = brand

    # Getter and Setter for km
    def get_km(self):
        return self._km

    def set_km(self, km):
        self._km = km

    # Getter and Setter for constructionYear
    def get_constructionYear(self):
        return self._constructionYear

    def set_constructionYear(self, constructionYear):
        self._constructionYear = constructionYear
    
    def __str__(self):
        return "Car(color: " + self._color + ", brand: " + self._brand + \
              ", km: " + str(self._km) + ", year: " + str(self._constructionYear) + ")"


# Bike class inheriting from Vehicle
class Bike(Vehicle):
    def __init__(self, color, tireNumber):
        super().__init__(color, tireNumber)

    def __str__(self):
        return "Bike(color: " + self._color + ")"

# Person class
class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.list_of_vehicles = []

    def add_vehicle(self, vehicle):
        self.list_of_vehicles.append(vehicle)

    def printVehicles(self):
        print(self.name, "has the following vehicles:")
        for v in self.list_of_vehicles:
            print(v)

# main
# Create instances of Car and Bike
car1 = Car("Red", 4, "Toyota", 50000, 2018)
car2 = Car("Black", 4, "Ford", 75000, 2020)
bike1 = Bike("Blue", 2)

# Create a Person and associate vehicles
person1 = Person("Alice", 101)
person1.add_vehicle(car1)
person1.add_vehicle(car2)
person1.add_vehicle(bike1)

# Print person's details and their vehicles
person1.printVehicles()
