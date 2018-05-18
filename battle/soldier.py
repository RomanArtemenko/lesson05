import random
from battle.unit import Unit

class Soldier(Unit):
    __counter = 0

    def __init__(self, health, recharge, experience=0):
        self.__class__.__counter += 1
        self.__id = self.__class__.__counter
        self.__experience = experience
        super().__init__(health, recharge)

    def __str__(self):
        return self.__class__.__name__ + "_" + str(self.__id)

    def __repr__(self):
        return self.__class__.__name__ + "_" + str(self.__id)

    @property
    def experience(self):
        return self.__experience

    # @experience.setter
    def add_experience(self):
        if self.experience < 50:
            self.__experience += 1

    def attack(self):
        return 0.5 * (1 + self.health / 100) * random.randrange(50 + self.__experience, 100) / 100

    def damage(self):
        return 0.05 + self.__experience / 100

    def get_id(self):
        return self.__id

    def name(self):
        return self.__class__.__name__ + "_" + str(self.__id)



