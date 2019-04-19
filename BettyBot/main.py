
"""
Betty the Bot
Project started on April 14th 2019
"""
import os
import time
from myHand import getHandInfo
from keys import selectCard , placeMySide
from all_charaters import *
from All_Spells import *
from EnemyPlaceSpots import IsEnemyPlaced

#constants
start_time = round(time.time(),1)
offical_Time = round(time.time(),1)
elixerAmount = 5
gainTime = int(2.8)
enemyCount = 0


while True:
    start = time.time()
    if (round(time.time(),1)- start_time) == gainTime:
        if elixerAmount < 10:
            elixerAmount += 1
        start_time = round(time.time(),1)
        print(f"elixer amount: {elixerAmount}")
    if (round(time.time(),1) - offical_Time) >= int(120.0):
        gainTime = int(1.4)

    myHand = getHandInfo()
    '''
    if myHand[0] == 'Giant':
        if Giant().get_cost <= elixerAmount:

            selectCard(1)
            placeMySide(120,530)
            elixerAmount -= Giant().get_cost

    if myHand[1] == 'Knight':
        if Knight().get_cost <= elixerAmount:
            selectCard(2)
            placeMySide(120,530)
            elixerAmount -= Knight().get_cost
    '''

    #else:
    #    pass
    #print(f"Loop Runs : {1/(time.time()-start)} Per Second")
