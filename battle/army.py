import battle.statisctics.statisctics as st

from battle.unit import Unit

class Army(Unit):

    def __init__(self, name, strategy, squads):
        self._name = name
        self._strategy = strategy
        self._squads = squads

    def __str__(self):
        return '%s "%s"' % (self.__class__.__name__ , self._name)

    @property
    def squads(self):
        return [sq for sq in self._squads if sq.active]

    @squads.setter
    def squads(self, squads):
        self._squads = squads

    @property
    def active(self):
        return bool(self.squads)

    @property
    def health(self):
        return round(st.mean([squad.health for squad in self.squads]) ,2)  

    def offensive(self, enemies):
        # print('-- Squads : %s' % self.squads)
        strike_force = self._get_target(self.squads)
        target_army = self._get_target(enemies)
        target_squad = self._get_target(target_army.squads)

        print("Армия " + self._name + " атакует армию " + target_army._name)
        target_squad.take_damage(strike_force.do_attack())

    def _get_target(self, obj):
        return self._strategy.select_enemy(obj)

    def attack(self):
        pass
 
    def damage(self):
        pass