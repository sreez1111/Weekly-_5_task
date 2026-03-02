class Vehicle:
    def __init__(self, brand, speed, fuel_type):
        self.brand = brand
        self.speed = speed
        self.fuel_type = fuel_type

    def display_info(self):
        print("Brand:", self.brand)
        print("Speed:", self.speed)
        print("Fuel Type:", self.fuel_type)


class Car(Vehicle):
    def __init__(self, brand, speed, fuel_type, number_of_doors):
        super().__init__(brand, speed, fuel_type)
        self.number_of_doors = number_of_doors

    def display_info(self):
        super().display_info()
        print("Number of Doors:", self.number_of_doors)
        print("---------------------------")


class Bike(Vehicle):
    def __init__(self, brand, speed, fuel_type, engine_capacity):
        super().__init__(brand, speed, fuel_type)
        self.engine_capacity = engine_capacity

    def display_info(self):
        super().display_info()
        print("Engine Capacity:", self.engine_capacity)
        print("---------------------------")


# Creating objects
car1 = Car("BMW", 250, "Diesel", 4)
bike1 = Bike("Bullet", 120, "Petrol", "350cc")

# Displaying details
car1.display_info()
bike1.display_info()