from unit import Unit

class Vehicle(Unit):
    def __init__(self, operators=3):
        self.operators = operators