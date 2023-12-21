class Node:
    def __init__(self, node, coord):
        self.node = node
        self.distFromStart = 0
        (self.x, self.y) = coord

    def distanceFromStart(self, map):
        if self.distFromStart != 0:
            return
        self.distFromStart += neighbourNode.distanceFromStart


class Map:
    def __init__(self, filelocation):
        self.map = []
        self.len_y = 0
        self.len_x = 0
        with open(filelocation) as file:
            for line in file.readlines():
                self.len_y += 1
                self.map += [char for char in line.strip()]
                self.len_x = len(line.strip())
                if 'S' in line:
                    self.startCoord = (line.index('S'),  self.len_y-1)
        print(f'Start coordonate is {self.startCoord}')

    def __call__(self, x, y):
        if x < 0 or y < 0 or x >= self.len_x or y >= self.len_y:
            return
        return self.map[x + y*self.len_x]
    
    def set(self,x, y, value):
        if x < 0 or y < 0 or x >= self.len_x or y >= self.len_y:
            return
        self.map[x + y*self.len_x] = value

Garden = Map('Day21/Input.txt')

def P1(Garden, nbStep):
    Distance = Garden
    for i in range(nbStep):

