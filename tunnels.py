import random as rand
import math

class MapMaker:
    def __init__(self, debug = False, num = 1, arraySize = 5,
                 tunnelCount = 5, maxLength = 5):
        
        self.debug = debug

        if arraySize > 0:
            self.arraySize = arraySize
        else:
            self.arraySize = 5

        if math.isfinite(num):
            self.num = num
        else:
            self.num = 1
        
        self.mapArray = self.createMap(num,self.arraySize)
        
        if tunnelCount > 0:
            self.tunnelCount = tunnelCount
        else:
            self.tunnelCount = this.arraySize
            
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
        self.mapArray[self.cur[0]][self.cur[1]] = 0

        self.displayMap()
        
        while self.tunnelCount > 0:

            print("===============")
            
            if self.debug:
                print("Digging....",end=" ")
                
            self.createTunnel()
            self.tunnelCount -= 1
            
            if self.debug:
                print("Done!")
                print("Tunnels left: " + str(self.tunnelCount))
            self.displayMap()
        

    def createMap(self,num,rows):
        newMap = []
        for i in range(rows):
            newMap.append([])
            for j in range(rows):
                newMap[i].append(num)
        return newMap

    def displayMap(self):
        for r in self.mapArray:
            print(str(r))

    def chooseLength(self):
        return rand.randrange(1,self.maxLength+1)

    def chooseDirection(self):

        if self.facing[0] == 0:
            self.facing = rand.choice([self.facingArray[0],self.facingArray[1]])
        else:
            self.facing = rand.choice([self.facingArray[2],self.facingArray[3]])

        return self.facing

    def choosecur(self):
        x = rand.randrange(0,5)
        y = rand.randrange(0,5)
        return [x,y]

    def createTunnel(self):
        self.facing = self.chooseDirection()
        tunnelLength = self.chooseLength()

        if self.debug:
            print("Cursor is currently at " + str(self.cur) +
                  " and facing " + str(self.facing))
            print("The tunnel will move " + str(tunnelLength) + " steps.")
        
        if self.facing[0] != 0:
            for i in range(0,tunnelLength):
                if self.debug:
                    print("Moving along the x axis...")

                if (self.cur[1] + self.facing[0] <= len(self.mapArray[0]) - 1 and
                    self.cur[1] + self.facing[0] >= 0):
                    
                    self.cur[1] = self.cur[1] + self.facing[0]
                    self.mapArray[self.cur[0]][self.cur[1]] = 0
                    
                elif (self.cur[1] + self.facing[0] > len(self.mapArray[0]) - 1):

                    self.cur[1] = 0
                    self.mapArray[self.cur[0]][self.cur[1]] = 0
                
                else:

                    self.cur[1] = len(self.mapArray[0]) - 1
                    self.mapArray[self.cur[0]][self.cur[1]] = 0
                
        if self.facing[1] != 0:
            if self.debug:
                print("Moving around the y axis...")

            for j in range(0,tunnelLength):
                if (self.cur[0] + self.facing[1] <= len(self.mapArray) - 1 and
                    self.cur[0] + self.facing[1] >= 0):

                    self.cur[0] = self.cur[0] + self.facing[1]
                    self.mapArray[self.cur[0]][self.cur[1]] = 0

                elif (self.cur[0] + self.facing[1] > len(self.mapArray) -1):

                    self.cur[0] = 0
                    self.mapArray[self.cur[0]][self.cur[1]] = 0
                    
                else:

                    self.cur[0] = len(self.mapArray) - 1
                    self.mapArray[self.cur[0]][self.cur[1]] = 0
                
        
        return self.mapArray

def fastPlay(rows = 5,tunnels = 5,ml = 5,debug = False):
    mm = MapMaker(debug,arraySize = rows,tunnelCount = tunnels, maxLength = ml)
    mm.play()
