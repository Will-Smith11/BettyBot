from Base import Charater

class Giant(Charater):
    """
    Giant
    note: rare card
    """
    def __init__(self):
        self.img = "Giant"
        self.cost = 5
        self.movementSpeed = "Slow"
        self.targets = "b"
        self.range = 0
        self.atktype = "tank"


class BabyDragon(Charater):
    """
    note: epic card
    """
    def __init__(self):
        self.img = "BabyDrag"
        self.cost = 4
        self.movementSpeed = "fast"
        self.targets = "ag"
        self.range = 3.5
        self.atktype = "support"

class SkellyArmy(Charater):
    """
    note: epic card
    """
    def __init__(self):
        self.img = "SkellyArmy"
        self.cost = 3
        self.movementSpeed = "fast"
        self.targets = "g"
        self.range = 0
        self.atktype = "defence"

class Minions(Charater):
    """
    note: common card
    """
    def __init__(self):
        self.img = "Minions"
        self.cost = 3
        self.movementSpeed = "fast"
        self.targets = "ag"
        self.range = 2
        self.atktype = "defence"

class Musketeer(Charater):
    """
    note: rare card
    """
    def __init__(self):
        self.img = "Musketeer"
        self.cost = 4
        self.movementSpeed = "medium"
        self.targets = "ag"
        self.range = 6
        self.atktype = "dmg"

class Knight(Charater):
    """
    note: common card
    """
    def __init__(self):
        self.img = "Knight"
        self.cost = 3
        self.movementSpeed = "medium"
        self.targets = "g"
        self.range = 0
        self.atktype = "defence"

class ThreeMusketeers(Charater):
    """
    Note:rare card
    """
    def __init__(self):
        self.cost = 10
        self.movementSpeed = "Medium"
        self.targets = "ag"
        self.range = 6
        self.atktype = "dmg"

class Golem(Charater):
    '''
    note: epic card
    '''
    def __init__(self):
        self.cost = 8
        self.movementSpeed = "slow"
        self.targets = "b"
        self.range = 0
        self.atktype = "tank"

class Witch(Charater):
    """
    note: epic card
    """
    def __init__(self):
        self.cost = 4
        self.movementSpeed = "Medium"
        self.targets = "ag"
        self.range = 5
        self.atktype = "support"

class Balloon(Charater):
    """
    note: epic card
    """
    def __init__(self):
        self.cost = 5
        self.movementSpeed = "medium"
        self.targets = "b"
        self.range = 0
        self.atktype = "dmg"

class Wizard(Charater):
    """
    note: rare card
    """
    def __init__(self):
        self.cost = 5
        self.movementSpeed = "medium"
        self.targets = "ag"
        self.range = 5.5
        self.atktype = "defence"

class GiantSkeleton(Charater):
    """
    note: epic card
    """
    def __init__(self):
        self.cost = 6
        self.movementSpeed = "medium"
        self.targets = "g"
        self.range = 0
        self.atktype = "defence"

class MegaKnight(Charater):
    """
    note: Legendary card!
    """
    def __init__(self):
        self.cost = 7
        self.movementSpeed = "medium"
        self.targets = "g"
        self.range = 0
        self.atktype = "dmg"

class MiniPekka(Charater):
    """
    note: rare card
    """
    def __init__(self):
        self.cost = 4
        self.movementSpeed = "fast"
        self.targets = "g"
        self.range = 0
        self.atktype = "dmg"
