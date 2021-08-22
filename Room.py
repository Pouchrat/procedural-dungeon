import random as rand

class Room:

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

        self.wall = "#"
        self.empty = "+"
        self.floor = " "
        self.door = " "
        self.spider = "x"
        self.rat = "o"
        self.chest = "a"
        self.potion = "i"

        self.maxSpider = maxSpider
        self.maxRat = maxRat
        self.maxChest = maxChest
        self.maxPotion = maxPotion

        self.minSpider = minSpider
        self.minRat = minRat
        self.minChest = minChest
        self.minPotion = minPotion

        self.roomArray = []
    
    def createRoom(self):
        rows = self.roomSize[0]
        cols = self.roomSize[1]

        self.roomArray = []
        
        for i in range(0,rows):
            self.roomArray.append([])
            for j in range(cols):
                if (i == 0 or i == self.roomSize[0] - 1 or
                    j == 0 or j == self.roomSize[1] - 1):
                    self.roomArray[i].append(self.wall)
                else:
                    self.roomArray[i].append(self.floor)

    def addDoors(self,doorCoord = None):
        if doorCoord == None:
            doorCoord = self.doorCoord

        doorPosX = int(self.roomSize[1]/2)
        doorPosY = int(self.roomSize[0]/2)

        if self.doorRand == True:
            for d in doorCoord:
                d = rand.randint(0,1)

        if doorCoord[0] == 1:
            self.roomArray[0][doorPosX] = self.door
            if self.roomSize[1] % 2 == 0:
                self.roomArray[0][doorPosX-1] = self.door

        if doorCoord[1] == 1:
            self.roomArray[doorPosY][self.roomSize[1]-1] = self.door
            if self.roomSize[0] % 2 == 0:
                self.roomArray[doorPosY-1][self.roomSize[1]-1] = self.door
                
        if doorCoord[2] == 1:
            self.roomArray[self.roomSize[0]-1][doorPosX] = self.door
            if self.roomSize[1] % 2 == 0:
                self.roomArray[self.roomSize[0]-1][doorPosX-1] = self.door

        if doorCoord[3] == 1:
            self.roomArray[doorPosY][0] = self.door
            if self.roomSize[0] % 2 == 0:
                self.roomArray[doorPosY-1][0] = self.door

    def createFilledRoom(self,fillType = None):
        if fillType == None:
            fillType = self.empty
        rows = self.roomSize[0]
        cols = self.roomSize[1]

        self.roomArray = []
        
        for i in range(0,rows):
            self.roomArray.append([])
            for j in range(cols):
                if self.debug:
                    self.roomArray[i].append(str(i+1) + "x" + str(j+1))
                else:
                    self.roomArray[i].append(fillType)
                

    def displayRoom(self):
        roomDisplay = ""
        itr = len(self.roomArray)
        for r in self.roomArray:
            for i in range(0,len(r)):
                roomDisplay += str(r[i])
                if i != len(r)-1:
                    roomDisplay += " "
            itr -= 1
            if itr > 0:
                roomDisplay += "\n"
        return roomDisplay

    def addItems(self,item,maxItem,minItem):

        row = rand.randrange(0,self.roomSize[0])
        col = rand.randrange(0,self.roomSize[1])
        itemCount = rand.randint(minItem,maxItem)

        while (itemCount > 0):
            if (self.roomArray[row][col] == self.floor):
                itemCount -= 1
                self.roomArray[row][col] = item
            else:
                row = rand.randint(0,self.roomSize[0]-1)
                col = rand.randint(0,self.roomSize[1]-1)
        
    def populateRoom(self):
        self.addItems(self.spider,self.maxSpider,self.minSpider)
        self.addItems(self.rat,self.maxRat,self.minRat)
        self.addItems(self.chest,self.maxChest,self.minChest)
        self.addItems(self.potion,self.maxPotion,self.minPotion)
