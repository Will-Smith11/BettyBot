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
        if np.allclose(img,giant,0,140):
            return "Giant"

        elif np.allclose(img,minions,0,150):
            return "Minions"

        elif np.allclose(img,knight,0,150):
            return "Knight"

        elif np.allclose(img,babyDragon,0,150):
            return "BabyDragon"

        elif np.allclose(img,skellyArmy,0,150):
            return "SkellyArmy"

        elif np.allclose(img,musketeer,0,150):
            return "Musketeer"

        elif np.allclose(img,arrows,0,150):
            return "Arrows"

        elif np.allclose(img,fireball,0,150):
            return "Fireball"
        return None

    except:
        pass
