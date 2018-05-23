from abc import ABCMeta, abstractmethod

class Unit(metaclass=ABCMeta):

    def __init__(self, name, clock, health=100, recharge=100):
        self._name = name
        self._health = health
        self._recharge = recharge
        self._recharge_end = 0
        self._clock = clock

    def __str__(self):
        return "%s %s" % (self.__class__.__name__ , self._name)

    def __repr__(self):
        return "%s %s" % (self.__class__.__name__ , self._name)

    def __gt__(self, obj):
        return self.health > obj.health

    def __lt__(self, obj):
        return self.health < obj.health

    def __eq__(self, obj):
        return self.health == obj.health

    def __le__(self, obj):
        return self.health <= obj.health

    def __ge__(self, obj):
        return self.health >= obj.health

    @abstractmethod
    def attack(self):
        pass
    
    @abstractmethod
    def damage(self):
        pass

    @property
    def active(self):
        return self._health > 0

    @property
    def health(self):
        return self._health  

    @health.setter
    def health(self, val):
        self._health = val

    @property
    def is_recharge(self):
        return self._recharge_end > self._clock.time

    def name(self):
        self._name



