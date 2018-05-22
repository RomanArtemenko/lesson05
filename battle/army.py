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

    

