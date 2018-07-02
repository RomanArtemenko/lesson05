import random
from battle.unit import Unit
from battle.soldier import Soldier
import battle.statisctics.statisctics as st



class Vehicle(Unit):

    def __init__(self, name, clock, health, operators):
        super().__init__(name, clock, health, 1000)
        self._operators = []
        for operator in operators:
            self.operators = operator
            
    @property
    def attack(self):
        return 0.5 * (1 + self.health / 100) * st.harmonic_mean([op.attack for op in self.operators])
    
    @property
    def damage(self):
        return 0.1 + sum([oper.experience / 100 for oper in self.operators])

    @property
    def health(self):
        return round(st.mean([super().health] + [operator.health for operator in self.operators]), 2)
    
    @property
    def operators(self):
        return [operator for operator in self._operators if operator.active]
    
    @operators.setter
    def operators(self, operator):
        if len(self.operators) < 3 and type(operator) is Soldier:
            self._operators.append(operator)

    @property
    def operators_active(self):
        return bool(self.operators)

    @property
    def active(self):
        return super().active and self.operators_active

    def take_damage(self, damage):
        self._health = self.health - damage * 0.6
        
        random_operator = random.choice(self.operators)

        for operator in self.operators:
            if random_operator is operator:
                operator.take_damage(damage * 0.1)
            operator.take_damage(damage * 0.1)

    def do_attack(self):
        self._recharge_end = self._clock.time + self._recharge_end

        for operator in self.operators:
            operator.do_attack()

        return self.damage

