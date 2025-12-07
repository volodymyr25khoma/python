class Card:
    """Class for users card"""

    def __init__(self, card_number, balance):
        if self.__check_attr_type(card_number, str):
            self._card_number = card_number
        if self.__check_attr_type(balance, float):
            self.__balance = balance

    def get_card_data(self):
        return self.__dict__

    def set_card_data(self, attr, value):
        if self.__check_attr_type(attr, str):
            self.__dict__[attr] = value
            return {attr: self.__dict__[attr]}
        else:
            return "Attribute must be string type"

    def __check_attr_type(self, attr, should_be):
        if type(attr) == should_be:
            return True
        else:
            raise TypeError(f"Attribute must be {should_be}")


user_card_1 = Card("4114 4114 5141 8949", 1000.0)
print(user_card_1.get_card_data)
print(user_card_1.set_card_data("card_number", "4114 0000 5141 8949"))
print(user_card_1.set_card_data("balance", 2000))
