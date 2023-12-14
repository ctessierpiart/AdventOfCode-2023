import copy

class Dish:
    def __init__(self, filelocation):
        self.map = []
        self.len_y = 0
        with open(filelocation) as file:
            for line in file.readlines():
                self.len_x = len(line.strip())
                self.map += [char for char in line.strip()]
                self.len_y += 1
        self.strainHistory = []

    def getLoc(self, x, y):
        if x >= self.len_x or x < 0 or y >= self.len_y or y < 0:
            return '#'
        return self.map[x + self.len_x*y]
    
    def setLoc(self, x, y, value):
        if x >= self.len_x or x < 0 or y >= self.len_y or y < 0:
            return 0
        self.map[x + y*self.len_x] = value
        return 1
    
    def idxToCoord(self, idx):
        x = idx % self.len_x
        y = idx // self.len_y
        return (x, y)
    
    def printMap(self):
        for i in range(self.len_y):
            print(self.map[i*self.len_x:(i+1)*self.len_x])
        print()

    def moveNorth(self):
        for idx, loc in enumerate(self.map):
            if loc == '#' or loc == '.':
                continue
            [Current_x, Current_y] = self.idxToCoord(idx)
            n = 1
            nextLoc = self.getLoc(Current_x, Current_y-n)
            while nextLoc == '.':
                n += 1
                nextLoc = self.getLoc(Current_x, Current_y-n)
            self.setLoc(Current_x, Current_y, '.')
            self.setLoc(Current_x, Current_y-n+1, 'O')

    def moveSouth(self):
        for idx, loc in enumerate(reversed(self.map)):
            idx = self.len_x * self.len_y - idx -1
            if loc == '#' or loc == '.':
                continue
            [Current_x, Current_y] = self.idxToCoord(idx)
            n = 1
            nextLoc = self.getLoc(Current_x, Current_y+n)
            while nextLoc == '.':
                n += 1
                nextLoc = self.getLoc(Current_x, Current_y+n)
            self.setLoc(Current_x, Current_y, '.')
            self.setLoc(Current_x, Current_y+n-1, 'O')

    def moveEast(self):
        for idx, loc in enumerate(reversed(self.map)):
            idx = self.len_x * self.len_y - idx -1
            if loc == '#' or loc == '.':
                continue
            [Current_x, Current_y] = self.idxToCoord(idx)
            n = 1
            nextLoc = self.getLoc(Current_x+n, Current_y)
            while nextLoc == '.':
                n += 1
                nextLoc = self.getLoc(Current_x+n, Current_y)
            self.setLoc(Current_x, Current_y, '.')
            self.setLoc(Current_x+n-1, Current_y, 'O')

    def moveWest(self):
        for idx, loc in enumerate(self.map):
            if loc == '#' or loc == '.':
                continue
            [Current_x, Current_y] = self.idxToCoord(idx)
            n = 1
            nextLoc = self.getLoc(Current_x-n, Current_y)
            while nextLoc == '.':
                n += 1
                nextLoc = self.getLoc(Current_x-n, Current_y)
            self.setLoc(Current_x, Current_y, '.')
            self.setLoc(Current_x-n+1, Current_y, 'O')

    def cycle(self, nCycle):
        self.strainHistory.append(self.getStrain())
        for i in range(nCycle):
            self.moveNorth()
            self.moveWest()
            self.moveSouth()
            self.moveEast()
            print(i, self.getStrain())
            self.strainHistory.append(self.getStrain())

    def getStrain(self):
        totalStrain = 0
        for idx, loc in enumerate(self.map):
            if loc == 'O':
                [_, Current_y] = self.idxToCoord(idx)
                totalStrain += self.len_y-Current_y
        return totalStrain
    
    def findCycle(self):
        oneTime = []
        twoTimes = []
        self.sequence_lenghts = 0
        self.sequence_start = 0
        self.sequence = []
        for idx, strain in enumerate(self.strainHistory):
            if strain in self.strainHistory[idx+1:]:
                findidx = self.strainHistory[idx+1:].index(strain) +1
                if findidx not in oneTime:
                    oneTime.append(findidx)
                elif findidx not in twoTimes:
                    twoTimes.append(findidx)
                else:
                    self.sequence_lenghts = findidx
                    self.sequence_start = idx
                    break

        for idx in range(self.sequence_start, self.sequence_start+self.sequence_lenghts):
            self.sequence.append(self.strainHistory[idx])

    def findStrain(self, nCycle):
        return self.sequence[(nCycle - self.sequence_start) %self.sequence_lenghts]



Part1 = Dish('Day14/Input.txt')
Part1.moveNorth()
print(f'Part 1 : {Part1.getStrain()}')

Part2 = Dish('Day14/Input.txt')
Part2.cycle(300)
Part2.findCycle()
print(f'Part 2 : {Part2.findStrain(1000000000)}')

