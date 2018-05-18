from battle.unit import Unit

class Vehicle(Unit):
    __operators = []
    __counter = 0

    def __init__(self, health, recharge, operator1=None, operator2=None, operator3=None):
        self.__class__.__counter += 1
        self.__id = self.__class__.__counter
        self.__operators.append(operator1)
        self.__operators.append(operator2)
        self.__operators.append(operator3)
        super().__init__(health, recharge)

    def __str__(self):
        return self.__class__.__name__ + "_" + str(self.__id)

    def __repr__(self):
        return self.__class__.__name__ + "_" + str(self.__id)
    
    @property
    def operators(self):
        return self.__operators
    
    @operators.setter
    def set_operator(self, operator):
        if len(self.__operators) < 3 and not operator is None:
            self.__operators.append(operator)

    def attack(self):
        return 111
        # 0.5 * (1 + self.health / 100) * gavg(operators.attack_success)

    def damage(self):
        return 0.1 + sum([oper.experience() / 100 for oper in self.operators()] )
