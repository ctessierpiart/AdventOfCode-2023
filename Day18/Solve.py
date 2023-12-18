class Edge:
    def __init__(self, line, startCoord):
        (self.start_x, self.start_y) = startCoord
        (self.end_x, self.end_y) = startCoord
        self.direction, self.length, self.color = line.split(' ')
        self.length = int(self.length) + 1
        if self.direction == 'U': 
            self.end_y -= (self.length - 1)
            self.step_x, self.step_y = 0, -1
        elif self.direction == 'D': 
            self.end_y += (self.length - 1)
            self.step_x, self.step_y = 0, 1
        elif self.direction == 'L': 
            self.end_x -= (self.length - 1)
            self.step_x, self.step_y = -1, 0
        elif self.direction == 'R': 
            self.end_x += (self.length - 1)
            self.step_x, self.step_y = 1, 0

    def useColor(self):
        lengthStr = self.color[2:-2]
        dirStr = self.color[-2]
        dir = ['R', 'D', 'L', 'U']
        dirStr = dir[int(dirStr)]
        lengthStr = str(int(lengthStr, 16))
        self.__init__(' '.join([dirStr, lengthStr, '_']), (self.start_x, self.start_y))
        
    def endCoord(self):
        return (self.end_x, self.end_y)
    
    def __repr__(self):
        return f'{(self.start_x, self.start_y)} => {(self.end_x, self.end_y)}'

class Map:
    def __init__(self, Edges):
        self.min_x = min([edge.end_x for edge in Edges])
        self.min_y = min([edge.end_y for edge in Edges])
        self.max_x = max([edge.end_x for edge in Edges])
        self.max_y = max([edge.end_y for edge in Edges])
        self.len_x = self.max_x-self.min_x + 1
        self.len_y = self.max_y-self.min_y + 1
        self.Edges = Edges
        self.terrain = [0] * (self.len_x * self.len_y)

    def get_off(self, x_off, y_off):
        return self.get(x_off-self.min_x, y_off-self.min_y)
    
    def get(self, x, y):
        if x < 0 or x >= self.len_x or y < 0 or y >= self.len_y:
            return None
        return self.terrain[x+ y*self.len_x]
    
    def set_off(self, x_off, y_off, value):
        self.set(x_off-self.min_x, y_off-self.min_y, value)

    def set(self, x, y, value):
        if x < 0 or x >= self.len_x or y < 0 or y >= self.len_y:
            return None
        if self.get(x, y) == 1: #Don't touch the edges
            return None
        self.terrain[x+ y*self.len_x] = value

    def Part1(self):
        for edge in self.Edges:
            if edge.step_x != 0:
                for idx in range(edge.start_x, edge.end_x, edge.step_x):
                    self.set_off(idx, edge.start_y, 1)
                    self.set_off(idx, edge.start_y + edge.step_x, 2)
            if edge.step_y != 0:
                for idx in range(edge.start_y, edge.end_y, edge.step_y):
                    self.set_off(edge.start_x, idx, 1)
                    self.set_off(edge.start_x - edge.step_y, idx, 2)

        diff = 1
        while diff != 0:
            diff = 0
            for idy in range(self.len_y):
                for idx in range(self.len_x):
                    if self.get(idx, idy) != 0:
                        continue
                    if self.check_neighbours(idx, idy, 2):
                        diff += 1
                        self.set(idx, idy, 2)

        for idx, value in enumerate(self.terrain):
            if value == 2:
                self.terrain[idx] = 1

        return sum(self.terrain)
    
    def makeContour(self, edgeBefore, edge, edgeAfter):
        ContourLength = edge.length - 1
        if edge.direction == 'R':
            if edgeBefore.direction == 'U' and edgeAfter.direction == 'D':
                ContourLength = edge.length
            elif edgeBefore.direction == 'D' and edgeAfter.direction == 'U':
                ContourLength = edge.length - 2
        elif edge.direction == 'L':
            if edgeBefore.direction == 'U' and edgeAfter.direction == 'D':
                ContourLength = edge.length - 2
            elif edgeBefore.direction == 'D' and edgeAfter.direction == 'U':
                ContourLength = edge.length
        elif edge.direction == 'U':
            if edgeBefore.direction == 'L' and edgeAfter.direction == 'R':
                ContourLength = edge.length
            elif edgeBefore.direction == 'R' and edgeAfter.direction == 'L':
                ContourLength = edge.length-2
        elif edge.direction == 'D':
            if edgeBefore.direction == 'L' and edgeAfter.direction == 'R':
                ContourLength = edge.length-2
            elif edgeBefore.direction == 'R' and edgeAfter.direction == 'L':
                ContourLength = edge.length
        
        config = ' '.join([edge.direction, str(ContourLength), '_'])
        return Edge(config, (edgeBefore.end_x, edgeBefore.end_y))

    def Part1_smarter(self):
        #make the true contour
        firstEdge = self.makeContour(Edges[-1], Edges[0], Edges[1])
        Contour = [firstEdge]
        for idx, edge in enumerate(Edges[1:-1]):
            Contour.append(self.makeContour(Contour[idx], edge, Edges[idx+2]))
        Contour.append(self.makeContour(Contour[-1], Edges[-1], Contour[0]))
        area = 0
        for contour in Contour:
            if contour.step_x != 0:
                area+= contour.step_x * (contour.length-1) * contour.start_y
        return abs(area)


    def check_neighbours(self, x, y, value):
        neighbours = [self.get(x, y-1), self.get(x, y+1), 
                      self.get(x-1, y), self.get(x+1, y)]
        if value in neighbours:
            return True
        return False


    def debug(self):
        for idy in range(self.len_y):
            print([self.get(idx, idy) for idx in range(self.len_x)])
        print()

Edges = []
with open('Day18/Input.txt') as file:
    coord = (0,0)
    for line in file.readlines():
        localEdge = Edge(line.strip(), coord)
        Edges.append(localEdge)
        coord = localEdge.endCoord()

Terrain = Map(Edges)
result = Terrain.Part1()
print(f'Part 1 : {result}')
result = Terrain.Part1_smarter()
print(f'Part 1 : {result}')

for edge in Edges:
    edge.useColor()
result = Terrain.Part1_smarter()
print(f'Part 2 : {result}')

