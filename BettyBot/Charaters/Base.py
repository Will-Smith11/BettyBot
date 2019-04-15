import os
import sys
import cv2
import numpy as np
class Charater():
    """
    Base class for all charaters
    """
    def __init__(self, cost,movementSpeed,img, atktype, range, targets):
        self.cost = cost
        self.movementSpeed = movementSpeed
        self.atktype = atktype
        self.range = range
        self.targets = targets
        self.has_spawnables = None
        self.img = img

    @property
    def get_img(self):
        return np.array(cv2.imread(os.path.join(os.path.dirname(__file__), 'Entity_Imgs',f'{self.img}.png'),0))

    @property
    def has_spawnables(self):
        return self.spawnables
    @property
    def get_target(self):
        return self.targets
    @property
    def get_cost(self):
        return self.cost
    @property
    def get_range(self):
        return self.range
    @property
    def get_atktype(self):
        return self.atktype
    @property
    def get_movementSpeed(self):
        return self.movementSpeed


class Spell:
    """
    base for all spells and throwables
    """
    def __init__(self, duration, cost, radius, targets, effects, img):
        self.duration = duration
        self.cost = cost
        self.radius = radius
        self.targets = targets
        self.effects = effects
        self.img = img

    @property
    def get_img(self):
        return np.array(cv2.imread(os.path.join(os.path.dirname(__file__), 'Entity_Imgs',f'{self.img}.png'),0))

    @property
    def get_duration(self):
        return self.duration
    @property
    def get_cost(self):
        return self.cost
    @property
    def get_radius(self):
        return self.radius
    @property
    def get_targets(self):
        return self.targets
    @property
    def get_effects(self):
        return self.effects
    @property
    def img(self):
        return self.img

class Building:
    """
    base for all building info
    """
    def __init__(self, duration, damage, spawnables, range, targets):
        self.duration = duration
        self.damage = damage
        self.spawnables = spawnables
        self.range = range
        self.targets = targets
