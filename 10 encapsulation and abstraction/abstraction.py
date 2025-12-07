from abc import ABC, abstractclassmethod


class Car(ABC):
    def __init__(self, mark, cost):
        self.mark = mark
        self.cost = cost

    @abstractclassmethod
    def car_preview(self):
        pass


class Toyota(Car):

    def car_preview(self):
        print(f"Car {self.mark} costs {self.cost}")


class Mercedes(Car):

    def car_preview(self):
        print(f"Car {self.mark} costs {self.cost}")


class Lanos(Car):
    pass


toyota = Toyota("offroad", 10000)
toyota.car_preview()
mercedes = Mercedes("crossover", 30000)
mercedes.car_preview()
print("_________________________________________________________")
# lanos = Lanos("classic", 1000)
# lanos не може бути реалізований, бо ми мусимо слідувати послідовності роботи з абстрактним класом,
# тобто реалізувати спочатку абстрактну функцію car_preview і тоді вже працювати з об'єктом

# ________________________________________________________________________________________________________


class Animal(ABC):

    @abstractclassmethod
    def move(self):
        pass

    @abstractclassmethod
    def eat(self):
        pass


class Cat(Animal):
    def __init__(self, color, age):
        self.color = color
        self.age = age

    def move(self):
        print(f"This cat is {self.color}")

    def eat(self):
        print(f"Cat is {self.age} years old")


class Dog(Animal):
    def __init__(self, hair, food):
        self.hair = hair
        self.food = food

    def move(self):
        print(f"Wow, that dog's {self.hair} hair is so comfort")

    def eat(self):
        print(f"Dog ate {self.food} two hours ago")


class Animal_2(Animal):
    pass


class Bird(Animal_2):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def move(self):
        print(f"Look, it's a {self.name}")

    def eat(self):
        print(f"That bird is like {self.size} size")


cat = Cat("ginger", 5)
cat.move()
cat.eat()

dog = Dog("fluffy", "meat")
dog.move()
dog.eat()

bird = Bird("sparrow", "small")
bird.move()
bird.eat()

animal = Animal_2()
animal.move()
animal.eat()

# ми не реалізували потрібних методів в класі Animal_2, тому і вибиває помилку
# система бачить це як абстрактний клас, бо в ньому вказано лише приналежність до батьківського класу, який теж є абстрактним
