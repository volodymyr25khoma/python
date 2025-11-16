class Point:
    """Class for coordinates"""

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.get_attrs()
        self.check_coords()

    def check_coords(self):
        for attrs in self.__dict__:
            if getattr(self, attrs, False) < 0:
                print("Coordinates can't be less than 0")
                setattr(self, attrs, 0)
            elif getattr(self, attrs, False) > 100:
                print("Coordinates can't be more than 100")
                setattr(self, attrs, 100)
        print(self.__dict__)

    def get_attrs(self):
        print(self.__dict__)

    def set_attrs(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


coord_1 = Point(-1, 101, 50)
