import time

class Dish:
    def __init__(self, filelocation):
        self.map = []
        self.len_y = 0
        with open(filelocation) as file:
            for line in file.readlines():
                self.len_x = len(line.strip())
                self.map += [char for char in line.strip()]
                self.len_y += 1

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
        t = time.time()
        for _ in range(nCycle):
            self.moveNorth()
            self.moveWest()
            self.moveSouth()
            self.moveEast()
        print(time.time() - t)

    def getStrain(self):
        totalStrain = 0
        for idx, loc in enumerate(self.map):
            if loc == 'O':
                [_, Current_y] = self.idxToCoord(idx)
                totalStrain += self.len_y-Current_y
        return totalStrain


Part1 = Dish('Day14/Input.txt')
Part1.moveNorth()
print(f'Part 1 : {Part1.getStrain()}')

Part2 = Dish('Day14/Input.txt')
Part2.cycle(1000)
print(f'Part 1 : {Part2.getStrain()}')

