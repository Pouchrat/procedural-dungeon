import DungeonMaker as DM


def play(debug = False):
    dm = DM.DungeonMaker(debug = debug)
    dm.play()
    dungeonOut = open("dungeon.txt","w")
    dungeonOut.write(dm.displayDungeon())
    dungeonOut.close()
