from battle.unit import Unit
import battle.statisctics.statisctics as st

class Squad(Unit):

    def __init__(self, units):
        self.units = units

    @property
    def units(self):
        return [unit for unit in self._units if unit.active]

    @units.setter
    def units(self, units):
        self._units = units

    @property
    def active(self):
        return bool(self.units)
    
    @property
    def attack(self):
        return st.harmonic_mean([unit.attack for unit in self.units]) 

    @property
    def damage(self):
        return sum([unit.damage for unit in self.units if not unit.is_recharge])

    @property
    def health(self):
        return round(st.mean([unit.health for unit in self.units]) ,2)

    def do_attack(self):
        for unit in self.units:
            unit.do_attack()
        return self.damage

    def take_damage(self, damage):
        for unit in self.units:
            unit.take_damage(damage / len(self.units))
