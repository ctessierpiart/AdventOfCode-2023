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

    def getStrain(self):
        totalStrain = 0
        for idx, loc in enumerate(self.map):
            if loc == 'O':
                [_, Current_y] = self.idxToCoord(idx)
                totalStrain += self.len_y-Current_y
        return totalStrain


Day14 = Dish('Day14/Input.txt')
Day14.moveNorth()
print(f'Part 1 : {Day14.getStrain()}')

