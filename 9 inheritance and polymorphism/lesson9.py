# наслідування в класах


class Vehicle:
    """Base of transport"""

    def __init__(self, type, color):
        self.type = type
        self.color = color

    def move(self):
        print("Your vehicle is moving")


class Car(Vehicle):
    """Class Car"""

    def __init__(self, type, color, cost=0):
        super().__init__(type, color)
        self.cost = cost

    def run_engine(self):
        print("Engine is running...")
        super().move()


class Bicycle(Vehicle):
    """Class Bicycle"""

    def __init__(self, type, color, chain_eff):
        super().__init__(type, color)
        self.chain_eff = chain_eff

    def check_chain_and_moving():
        print("Chain is alright, let's go cycling!")


car_1 = Car("car", "white", 20000)
car_1.run_engine()
