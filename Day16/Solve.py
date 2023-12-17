class Beam:
    def __init__(self, startCoord, orientation):
        (self.x, self.y) = startCoord
        self.startCoord = startCoord
        self.orientation = orientation
    
    def __repr__(self):
        return f'{self.startCoord}' + self.orientation
    
    def move(self):
        if self.orientation == 'U':
            self.y -= 1
        elif self.orientation == 'D':
            self.y += 1
        elif self.orientation == 'L':
            self.x -= 1
        elif self.orientation == 'R':
            self.x += 1
    
    def process(self, contraption):
        if self.__repr__() in contraption.Beams:
            return 
        tile = contraption.get(self.x, self.y)
        contraption.enlighten(self.x, self.y)
        while tile == '.':
            self.move()
            contraption.enlighten(self.x, self.y)
            tile = contraption.get(self.x, self.y)
        if tile in contraption.elements:
            if tile == '/':
                if self.orientation == 'R': return [Beam((self.x, self.y - 1), 'U')]
                elif self.orientation == 'L': return [Beam((self.x, self.y + 1), 'D')]
                elif self.orientation == 'U': return [Beam((self.x + 1, self.y), 'R')]
                elif self.orientation == 'D': return [Beam((self.x - 1, self.y), 'L')]
            elif tile == '?': # '\'
                if self.orientation == 'R': return [Beam((self.x, self.y + 1), 'D')]
                elif self.orientation == 'L': return [Beam((self.x, self.y - 1), 'U')]
                elif self.orientation == 'U': return [Beam((self.x - 1, self.y), 'L')]
                elif self.orientation == 'D': return [Beam((self.x + 1, self.y), 'R')]
            elif tile == '-':
                if self.orientation == 'R': return [Beam((self.x + 1, self.y), 'R')]
                elif self.orientation == 'L': return [Beam((self.x - 1, self.y), 'L')]
                elif self.orientation == 'U' or self.orientation == 'D':
                    return [Beam((self.x - 1, self.y), 'L'), Beam((self.x + 1, self.y), 'R')]
            elif tile == '|':
                if self.orientation == 'U': return [Beam((self.x, self.y - 1), 'U')]
                elif self.orientation == 'D': return [Beam((self.x, self.y + 1), 'D')]
                elif self.orientation == 'R' or self.orientation == 'L':
                    return [Beam((self.x, self.y - 1), 'U'), Beam((self.x, self.y + 1), 'D')]
                 
class Contraption:
    def __init__(self, filelocation):
        self.map = ''
        self.len_y = 0
        with open(filelocation) as file:
            for line in file.readlines():
                line = line.strip().replace('\\', '?')
                self.map += line.strip()
                self.len_y += 1
                self.len_x = len(line.strip())
        self.Beams = {}
        self.lightened = [0] * self.len_x * self.len_y
        self.elements = ['/', '-', '|', '?']
                
    def get(self, x, y):
        if (x >= self.len_x) or (x < 0) or (y >= self.len_y) or (y < 0):
            return 0
        return self.map[x + y*self.len_x]
    
    def enlighten(self, x, y):
        if (x >= self.len_x) or (x < 0) or (y >= self.len_y) or (y < 0):
            return 
        self.lightened[x + y*self.len_x] = 1
    
    def processLight(self, StartBeam):
        self.Beams = {}
        self.lightened = [0] * self.len_x * self.len_y
        beamsToProcess = [StartBeam]
        nextBeams = []
        while beamsToProcess != []:
            for beam in beamsToProcess:
                beam_result = beam.process(self)
                self.Beams[repr(beam)] = beam
                if beam_result != None:
                    for beamToappend in beam_result:
                        nextBeams.append(beamToappend)
            beamsToProcess = nextBeams
            nextBeams = []
        
        return sum(self.lightened)
            
    def Part1_result(self):
        result = self.processLight(Beam((0,0), 'R'))
        print(f'Part 1 : {result}') 

        
    def Part2_result(self):
        maxLight = 0
        for start in range(self.len_x):
            maxLight = max([maxLight, self.processLight(Beam((0,start), 'R'))])
        for start in range(self.len_x):
            maxLight = max([maxLight, self.processLight(Beam((self.len_x-1,start), 'L'))])
        for start in range(self.len_y):
            maxLight = max([maxLight, self.processLight(Beam((start, 0), 'D'))])
        for start in range(self.len_y):
            maxLight = max([maxLight, self.processLight(Beam((start, self.len_y-1), 'U'))])
        print(f'Part 2 : {maxLight}')
            
            
        
    def debugLighten(self):
        for i in range(self.len_y):
            print(''.join(str(value) for value in self.lightened[i*self.len_x: (i+1)*self.len_x]))
                
Puzzle = Contraption('Day16/Input.txt')
Puzzle.Part1_result()
Puzzle.Part2_result()

                
                