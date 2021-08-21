import Room as r

class RoomMaker:
    def __init__(self, roomSize = [10,25], doorCoord = [1,1,1,1], # [N,E,S,W]
                 doorRand = False, doorNum = 1,
                 maxSpider = 3, maxRat = 3, maxChest = 1, maxPotion = 2,
                 minSpider = 1, minRat = 1, minChest = 1, minPotion = 1,
                 debug = False):
        
        self.debug = debug
        self.doorRand = doorRand

        self.roomSize = roomSize
        self.doorCoord = doorCoord
        self.doorNum = doorNum

        self.maxSpider = maxSpider
        self.maxRat = maxRat
        self.maxChest = maxChest
        self.maxPotion = maxPotion

        self.minSpider = minSpider
        self.minRat = minRat
        self.minChest = minChest
        self.minPotion = minPotion

        self.room = None
        

    def play(self):
        self.createRoom()
        self.populateRoom()
        self.addDoors()

    def createRoom(self):
        self.room = r.Room(self.roomSize,debug=self.debug)
        self.room.createRoom()

    def addDoors(self,doorCoord = None):
        if doorCoord == None:
            doorCoord = self.doorCoord
        if self.room != None:
            self.room.addDoors(doorCoord)
            return True
        else: return False

    def createWallRoom(self):
        self.room = r.Room(self.roomSize,doorCoord = [0,0,0,0],debug=self.debug)
        self.room.createWallRoom()
                

    def displayRoom(self):
        if self.room != None:
            return self.room.displayRoom()
        else: return ""

    def addItems(self,item,maxItem,minItem):
        if self.room != None:
            self.room.addItems(item,maxItem,minItem)
            return True
        else: return False
        
    def populateRoom(self):
        if self.room != None:
            self.room.populateRoom()
            return True
        else: return False


