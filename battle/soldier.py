import random
from battle.unit import Unit

class Soldier(Unit):

    def __init__(self, name, clock, health, recharge, experience=0):
        super().__init__(name, clock, health, recharge)
        self._experience = experience

    @property
    def attack(self):
        return 0.5 * (1 + self.health / 100) * random.randrange(50 + self._experience, 100) / 100

    @property
    def damage(self):
        return 0.05 + self._experience / 100

    @property
    def experience(self):
        return self._experience

    def add_experience(self):
        if self.experience < 50:
            self._experience += 1   

    def do_attack(self):
        self.add_experience()
        return self.attack

    def take_damage(self, damage):
        self._health = self.health - damage