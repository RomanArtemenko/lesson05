from battle.unit import Unit

class Soldier(Unit):
    def __init__(self, experience=0):
        self.experience = experience
        # super().__init__(self, health, recharge)

    def attack():
        return 0.5 * (1 + self.health / 100) * random(50 + self.experience, 100) / 100