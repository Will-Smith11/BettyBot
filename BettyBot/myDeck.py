from all_charaters import Giant , Knight, SkellyArmy , Minions
from all_charaters import Musketeer, BabyDragon
from All_Spells import Arrows, Fireball
import numpy as np


giant = Giant().get_img
knight = Knight().get_img
skellyArmy = SkellyArmy().get_img
minions = Minions().get_img
musketeer = Musketeer().get_img
babyDragon =  BabyDragon().get_img
arrows = Arrows().get_img
fireball = Fireball().get_img


def check_for_match(img):

    if np.allclose(img,giant,0,100):
        return "giant"
    if np.allclose(img,knight,0,100):
        return "knight"
    if np.allclose(img,skellyArmy,0,100):
        return "skellyArmy"
    if np.allclose(img,minions,0,100):
        return "minions"
    if np.allclose(img,musketeer,0,100):
        return "musketeer"
    if np.allclose(img,babyDragon,0,100):
        return "babyDragon"
    if np.allclose(img,arrows,0,100):
        return "arrows"
    if np.allclose(img,fireball,0,100):
        return "fireball"
    return
