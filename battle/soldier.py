import random
from battle.unit import Unit

class Soldier(Unit):
    __counter = 0

    def __init__(self, health, recharge, experience=0):
        self.__class__.__counter += 1
        self.__id = self.__class__.__counter
        self.__experience = experience
        super().__init__(health, recharge)

    def attack(self):
        return 0.5 * (1 + self.health / 100) * random.randrange(50 + self.__experience, 100) / 100

    def damage(self):
        return 0.05 + self.__experience / 100

    def get_name(self):
        return self.__class__.__name__ + str(self.__id)

    def get_id(self):
        return self.__id