import battle.statisctics.statisctics as st

class Army:

    def __init__(self, name, strategy, squads):
        self._name = name
        self._strategy = strategy
        self.squads = squads

    @property
    def squads(self):
        return [squad for squad in self.squads if squad.active]

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
        strike_force = self._get_target(self.squads)
        target_army = self._get_target(enemies)
        target_squad = self._get_target(target_army.squads)

        print("Армия " + self.name + " атакует армию " + target_army.name)
        target_squad.take_damage(strike_force.do_attack())

    def _get_target(self, obj):
        return self._strategy.select_enemy(obj)
        


    

