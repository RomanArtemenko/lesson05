from abc import ABCMeta, abstractmethod

 class Strategy(metaclass=ABCMeta):

     @abstractmethod
     def select_squad(self, army):
         pass

 class RandomStrategy(Strategy):
     pass

 class WeakestStrategy(Strategy):
     pass

 class StrongestStrategy(Strategy):
     pass

