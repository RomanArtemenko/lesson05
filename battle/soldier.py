import random
from battle.unit import Unit

class Soldier(Unit):
    def __init__(self, health, recharge, experience=0):
        self._experience = experience
        super().__init__(health, recharge)

    def attack(self, target):
        return 0.5 * (1 + self.health / 100) * random(50 + self._experience, 100) / 100

    def take_damage(self):
        pass

    def alive(self):
        pass