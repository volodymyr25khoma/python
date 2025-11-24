# поліморфізм через наслідування


class Vehicle:
    """Base of transport"""

    def __init__(self, type, color, efficiency):
        self.type = type
        self.color = color
        self.efficiency = efficiency

    def move(self):
        print("Your vehicle is moving")

    def check(self):
        if self.efficiency <= 50:
            print(f"{self.type} is need to be fixed")
        else:
            print(f"{self.type} is good, keep moving!")


class Car(Vehicle):
    """Class Car"""

    def __init__(self, type, color, efficiency, cost=0):
        super().__init__(type, color, efficiency)
        self.cost = cost

    def move(self):
        print(f"{self.color} {self.type} is moving")
        print(f"Cost of this car: {self.cost}")


class Bicycle(Vehicle):
    """Class Bicycle"""

    def __init__(self, type, color, efficiency, chain_eff):
        super().__init__(type, color, efficiency)
        self.chain_eff = chain_eff

    def move(self):
        print("Let's go cycling!")


car_1 = Car("car", "white", 70, 20000)
car_1.move()
car_1.check()
bicycle_1 = Bicycle("road_bicycle", "red", 30, 1500)
bicycle_1.move()
bicycle_1.check()
