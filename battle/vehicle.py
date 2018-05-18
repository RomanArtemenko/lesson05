from unit import Unit


class Vehicle(Unit):
    __operators = []

    def __init__(self, operators=3):
        self.__operators = operators

    def attack(self):
        pass

    def damage(self):
        pass
