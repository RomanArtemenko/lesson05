from abc import ABCMeta, abstractmethod

class Unit(metaclass=ABCMeta):

    def __init__(self, name, health=100, recharge=100):
        self._name = name
        self._health = health
        self._recharge = recharge

    def __str__(self):
        return "%s %s" % (self.__class__.__name__ , self._name)

    def __repr__(self):
        return "%s %s" % (self.__class__.__name__ , self._name)

    @abstractmethod
    def attack(self):
        pass
    
    @abstractmethod
    def damage(self):
        pass

    @property
    def alive(self):
        return self._health > 0

    @property
    def health(self):
        return self._health

    def name(self):
        self._name



