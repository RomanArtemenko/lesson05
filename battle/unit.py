from abc import ABCMeta, abstractmethod

class Unit(metaclass=ABCMeta):
    # __counter = 0

    def __init__(self, health=100, recharge=100):
        # self.__class__.__counter += 1
        # self.__id = self.__class__.__counter
        self.__health = health
        self.__recharge = recharge

    @abstractmethod
    def attack(self):
        pass
    
    @abstractmethod
    def damage(self):
        pass

    @property
    def alive(self):
        return self.__health > 0

    @property
    def health(self):
        return self.__health