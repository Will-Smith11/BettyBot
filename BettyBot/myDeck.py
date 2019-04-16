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
    try:
        if np.allclose(img,giant,0,160):
            return "giant"

        elif np.allclose(img,minions,0,170):
            return "minions"

        elif np.allclose(img,knight,0,160):
            return "knight"

        elif np.allclose(img,babyDragon,0,185):
            return "babyDragon"

        elif np.allclose(img,skellyArmy,0,160):
            return "skellyArmy"

        elif np.allclose(img,musketeer,0,185):
            return "musketeer"

        elif np.allclose(img,arrows,0,160):
            return "arrows"

        elif np.allclose(img,fireball,0,160):
            return "fireball"
        return None

    except Exception as e:
        return (e.message, e.args)
