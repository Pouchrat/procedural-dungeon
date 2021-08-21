import random as rand
import math
import RoomMaker as RM
import DungeonMaker as DM


def play(debug = False):
    dm = DM.DungeonMaker(debug = debug)
    dm.play()
