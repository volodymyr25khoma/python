class BaseInterface:
    """Base class"""

    def __init__(self):
        pass

    def get_attrs(self):
        pass

    def print_model(self):
        pass

    def pricing(self):
        pass

    def support_call(self):
        pass


class SiteInterface(BaseInterface):
    """Interface of our site"""

    def __init__(self, number, model, price):
        super().__init__()
        self.number = number
        self.model = model
        self.price = price

    def print_model(self):
        print(f"Model of site: {self.model}")

    def pricing(self):
        print(f"Count of site price: {self.price ** 2}")

    def support_call(self):
        print(f"Number of support: {self.number}")
        print("Available at 8am - 8pm")


class AppInterface(BaseInterface):
    """Interface of our application"""

    def __init__(self, number, model, price):
        super().__init__()
        self.number = number
        self.model = model
        self.price = price

    def print_model(self):
        print(f"Model of application: {self.model}")

    def pricing(self):
        print(f"Count of application price: {self.price ** 2}")

    def support_call(self):
        print(f"Number of support: {self.number}")
        print("Available at 8am - 8pm")


site_user = SiteInterface(12345, "shop", 1000)
app_user = AppInterface(54314, "mac", 800)

for user in (site_user, app_user):
    user.print_model()
    user.pricing()
    user.support_call()
    print("_________________")
