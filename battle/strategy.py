import random
from abc import ABCMeta, abstractmethod

class Strategy(metaclass=ABCMeta):

    @abstractmethod
    def select_enemy(self, enemy):
        pass

class RandomStrategy(Strategy):
    
    def select_enemy(self, enemy):
        return random.choice(enemy)

class WeakestStrategy(Strategy):
    
    def select_enemy(self, enemy):
        return min(enemy)

class StrongestStrategy(Strategy):
    
    def select_enemy(self, enemy):
        return max(enemy)

