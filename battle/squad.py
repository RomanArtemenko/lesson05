from battle.unit import Unit

class Squad(Unit):

    def __init__(self, units):
        self._units

    @property
    def units(self):
        return self._units

    @units.setter
    def units(self, units):
        self._units = units

    @property
    def active(self):
        for unit in self.units:
            if unit.active:
                return True
        return False
    
    @property
    def attack(self):
        return 1 

    @property
    def damage(self):
        return 1

    def do_attack(self):
        pass

    def take_damage(self, damage):
        active_units = [unit for unit in self.units if unit.active]
        unit_damage = damage / len(active_units)
        for unit in active_units:
            unit.take_damage(unit_damage)
