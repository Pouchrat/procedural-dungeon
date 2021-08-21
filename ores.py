import random as rand
import math

class MapMaker:
    def __init__(self, debug = False, ground = "#", goldCount = 5, ironCount = 5,
                 arraySize = 5, veinCount = 5, maxLength = 5):
        
        self.debug = debug

        if arraySize > 0:
            self.arraySize = arraySize
        else:
            self.arraySize = 5

        self.ground = ground
        self.gold = "g"
        self.iron = "I"

        self.ores = [self.gold,self.iron]
        
        self.mapArray = self.createMap(ground,self.arraySize)
        
        if veinCount > 0:
            self.veinCount = veinCount
        else:
            self.veinCount = this.arraySize
            
        if maxLength > 0:
            self.maxLength = maxLength
        else:
            self.maxLength = this.arraySize
        
        self.facingArray = [[1,0], # Right
                           [-1,0], # Left
                           [0,1],  # Down
                           [0,-1]] # Up
        self.facing = self.facingArray[0]


    def play(self):
        self.cur = self.choosecur()
        
        while self.veinCount > 0:
            
            if self.debug:
                print("===============")
                print("Digging....",end=" ")
                
            self.createVein()
            self.veinCount -= 1
            
            if self.debug:
                print("Done!")
                print("Veins left: " + str(self.veinCount))
                self.displayMap()
        self.displayMap()
        

    def createMap(self,ground,rows):
        newMap = []
        for i in range(rows):
            newMap.append([])
            for j in range(rows):
                newMap[i].append(ground)
        return newMap

    def displayMap(self):
        for r in self.mapArray:
            for i in range(0,len(r)):
                print(str(r[i]),end=" ")
            print()

    def chooseLength(self):
        return rand.randrange(1,self.maxLength+1)

    def chooseDirection(self):

        if self.facing[0] == 0:
            self.facing = rand.choice([self.facingArray[0],self.facingArray[1]])
        else:
            self.facing = rand.choice([self.facingArray[1],self.facingArray[2]])

        return self.facing

    def choosecur(self):
        x = rand.randrange(0,5)
        y = rand.randrange(0,5)
        return [x,y]
    
    def chooseOre(self):
        return rand.choice(self.ores)

    def createVein(self):
        self.facing = self.chooseDirection()
        ore = self.chooseOre()
        veinLength = self.chooseLength()

        if self.debug:
            print("Cursor is currently at " + str(self.cur) +
                  " and facing " + str(self.facing))
            print("The vein will move " + str(veinLength) + " steps.")
        
        if self.facing[0] != 0:
            for i in range(0,veinLength):
                if self.debug:
                    print("Moving along the x axis...")

                if (self.cur[1] + self.facing[0] <= len(self.mapArray[0]) - 1 and
                    self.cur[1] + self.facing[0] >= 0):
                    
                    self.cur[1] = self.cur[1] + self.facing[0]
                    self.mapArray[self.cur[0]][self.cur[1]] = ore
                    
                elif (self.cur[1] + self.facing[0] > len(self.mapArray[0]) - 1):

                    self.cur[1] = 0
                    self.mapArray[self.cur[0]][self.cur[1]] = ore
                
                else:

                    self.cur[1] = len(self.mapArray[0]) - 1
                    self.mapArray[self.cur[0]][self.cur[1]] = ore
                
        if self.facing[1] != 0:
            if self.debug:
                print("Moving around the y axis...")

            for j in range(0,veinLength):
                if (self.cur[0] + self.facing[1] <= len(self.mapArray) - 1 and
                    self.cur[0] + self.facing[1] >= 0):

                    self.cur[0] = self.cur[0] + self.facing[1]
                    self.mapArray[self.cur[0]][self.cur[1]] = ore

                elif (self.cur[0] + self.facing[1] > len(self.mapArray) -1):

                    self.cur[0] = 0
                    self.mapArray[self.cur[0]][self.cur[1]] = ore
                    
                else:

                    self.cur[0] = len(self.mapArray) - 1
                    self.mapArray[self.cur[0]][self.cur[1]] = ore
                
        
        return self.mapArray

def fastPlay(rows = 5,veins = 5,ml = 5,debug = False):
    mm = MapMaker(debug,arraySize = rows,veinCount = veins, maxLength = ml)
    mm.play()
