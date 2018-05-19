import random
from battle.unit import Unit

class Soldier(Unit):

    def __init__(self, name, health, recharge, experience=0):
        super().__init__(name, health, recharge)
        self._experience = experience

    @property
    def experience(self):
        return self._experience

    def add_experience(self):
        if self.experience < 50:
            self._experience += 1

    def attack(self):
        return 0.5 * (1 + self.health / 100) * random.randrange(50 + self._experience, 100) / 100

    def damage(self):
        return 0.05 + self._experience / 100




