from abc import ABCMeta, abstractmethod

class Unit(metaclass=ABCMeta):
    def __init__(self, health=100, recharge=100):
        self._health = health
        self._recharge = recharge

    @abstractmethod
    def attack(self, target):
        pass
    
    @abstractmethod
    def take_damage(self):
        pass

    @property
    @abstractmethod
    def alive(self):
        pass

    @property
    def health(self):
        return self._health

