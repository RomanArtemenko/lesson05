import random
from battle.unit import Unit

class Soldier(Unit):

    def __init__(self, name, clock, health, experience=1):
        super().__init__(name, clock, health)
        self._experience = experience

    @property
    def attack(self):
        return 0.5 * (1 + self.health / 100) * random.uniform(50 + self.experience, 100) / 100

    @property
    def damage(self):
        return 0.05 + self._experience / 100

    @property
    def experience(self):
        return self._experience

    def add_experience(self, val):
        if self.experience < 50:
            self._experience += val   

    def do_attack(self):
        self.add_experience(self.attack + self.damage)
        self._recharge_end = self._clock.time + self._recharge_end
        
        return self.damage

    def take_damage(self, damage):
        self._health = self.health - damage