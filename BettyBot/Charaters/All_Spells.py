from Base import Spell



class Fireball(Spell):
    """
    note: sorta good
    """
    def __init__(self):
        self.img = "Fireball"
        self.duration = 0
        self.cost = 4
        self.targets = "ag"
        self.radius = 2.5
        self.effects = "dmg"

class Arrows(Spell):
    """
    note: good at taking out big groups
    of enemys
    """
    def __init__(self):
        self.img = "Arrows"
        self.duration = 0
        self.cost = 3
        self.targets = "ag"
        self.radius = 4
        self.effects = "dmg"
