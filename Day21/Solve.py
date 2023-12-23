import sys
sys. setrecursionlimit(1000000)

class Node:
    def __init__(self, node, coord):
        self.node = node
        self.distFromStart = None
        (self.x, self.y) = coord
        self.coord = coord
        self.checked = False
        self.isStep = False

    def validNeighbours(self, map, value):
        self.distFromStart = value
        if self.checked:
            return
        self.checked = True
        validNodes = []
        for coord in [(self.x, self.y-1), (self.x, self.y+1), 
                      (self.x+1, self.y), (self.x-1, self.y)]:
            neighbours = map(coord)
            if neighbours != None and neighbours.node == '.' and not neighbours.checked:
                validNodes.append(neighbours)
        return validNodes

    def __repr__(self):
        return f'{self.coord} : "{self.node}"'


class Map:
    def __init__(self, filelocation):
        self.map = []
        self.len_y = 0
        self.len_x = 0
        with open(filelocation) as file:
            for line in file.readlines():
                self.len_y += 1
                for idx, char in enumerate(line.strip()):
                    self.map.append(Node(char, (idx, self.len_y-1)))
                self.len_x = len(line.strip())
                if 'S' in line:
                    self.startCoord = (line.index('S'),  self.len_y-1)
        print(f'Start coordonate is {self.startCoord}')

    def __call__(self, coord):
        (x, y) = coord
        if x < 0 or y < 0 or x >= self.len_x or y >= self.len_y:
            return
        return self.map[x + y*self.len_x]
    
    def set(self,x, y, value):
        if x < 0 or y < 0 or x >= self.len_x or y >= self.len_y:
            return
        self.map[x + y*self.len_x] = value

    def solveP1(self, nbstep):
        nodeToProcess = [self(self.startCoord)]
        nodeNext = []
        step = 0
        while len(nodeToProcess) > 0:
            for node in nodeToProcess:
                neighbours = node.validNeighbours(self, step)
                if neighbours == None:
                    continue
                nodeNext += neighbours
            nodeToProcess = nodeNext
            nodeNext = []
            step += 1
        self.debug()    
        nbpos = 0
        ref = nbstep%2 #little optimisation
        for node in self.map:
            if node.distFromStart != None and node.distFromStart <= nbstep:
                if node.distFromStart%2 == ref:
                    nbpos += 1
                    node.isStep = True #for debug
        return nbpos
    
    def solveP2(self, nbstep): #samething but on the fly
        nbpos = 0
        ref = nbstep%2
        nodeToProcess = [self(self.startCoord)]
        nodeNext = []
        for step in range(nbstep+1):
            if step%2 == ref:
                nbpos += len(nodeToProcess)
            for node in nodeToProcess:
                neighbours = node.validNeighbours(self, step)
                if neighbours == None:
                    continue
                nodeNext += neighbours
            nodeToProcess = nodeNext
            nodeNext = []
        return nbpos


    def debug(self):
        for i in range(self.len_y):
            print([self((idx, i)).distFromStart for idx in range(self.len_x)])
        print()
        for node in self.map:
            if node.distFromStart == 0:
                print('?NNNNN')
                print(node.coord)

Garden = Map('Day21/Example.txt')

print(f'Part 1 {Garden.solveP1(6)}')
print(f'Part 1 {Garden.solveP2(6)}')

try