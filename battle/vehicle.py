from battle.unit import Unit
import battle.statisctics.statisctics as st

class Vehicle(Unit):
    _operators = []


    def __init__(self, name, health, recharge, operator1=None, operator2=None, operator3=None):
        super().__init__(name, health, recharge)
        self._operators.append(operator1)
        self._operators.append(operator2)
        self._operators.append(operator3)

    @property
    def operators(self):
        return self._operators
    
    @operators.setter
    def set_operator(self, operator):
        if len(self._operators) < 3 and not operator is None:
            self._operators.append(operator)

    def attack(self):
        return 0.5 * (1 + self.health / 100) * st.harmonic_mean([op.attack() for op in self.operators])
        # return 0.5 * (1 + self.health / 100) * st.harmonic_mean([1, 2, 4])

    def damage(self):
        return 0.1 + sum([oper.experience() / 100 for oper in self.operators] )
