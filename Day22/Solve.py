class Brick:
    def __init__(self, line, start_z = 0):
        if isinstance(line, str):
            begin_coord_str, end_coord_str = line.split('~')
            self.coord_begin = [int(char) for char in begin_coord_str.split(',')]
            self.coord_end = [int(char) for char in end_coord_str.split(',')]
        else:
            self.coord_begin = line.coord_begin
            self.coord_end = line.coord_end
            delta = self.coord_begin[2] - start_z
            self.coord_end[2] -= delta
            self.coord_begin[2] -= delta
        (self.x1, self.y1, self.z1) = self.coord_begin
        (self.x2, self.y2, self.z2) = self.coord_end
        self.contact_above = []
        self.contact_below = []
        self.lowest_point = min(self.z1, self.z2)
        self.highest_point = max(self.z1, self.z2)
        
    def __repr__(self):
        return f'{self.coord_begin}~{self.coord_end}'

class Space:
    def __init__(self, filelocation):
        self.bricks = []
        with open(filelocation) as file:
            for line in file.readlines():
                self.bricks.append(Brick(line.strip()))
        self.len = len(self.bricks)
        self.bricks.sort(key= lambda brick:brick.lowest_point)
        self.settle = []
        for idx_brick, brick in enumerate(self.bricks):
            new_brick = None
            for settled_brick in reversed(self.settle):
                if self.check_overlap(brick, settled_brick):
                    new_brick = Brick(brick, settled_brick.highest_point+1)
                    break
            if new_brick == None:
                new_brick = Brick(brick, 0)
            self.settle.append(new_brick)
                
    def get_brick(self, idx):
        if idx < 0 or idx >= self.len:
            return None
        return self.bricks[idx]

    def check_overlap(self, brick1, brick2):
        f3 = ((brick2.x1 - brick1.x1)*(brick1.y2 - brick1.y1) -
              (brick2.y1 - brick1.y1)*(brick1.x2 - brick1.x1))
        f4 = ((brick2.x2 - brick1.x1)*(brick1.y2 - brick1.y1) -
              (brick2.y2 - brick1.y1)*(brick1.x2 - brick1.x1))
        g1 = ((brick1.x1 - brick2.x1)*(brick2.y2 - brick2.y1) -
              (brick1.y1 - brick2.y1)*(brick2.x2 - brick2.x1))
        g2 = ((brick1.x2 - brick2.x1)*(brick2.y2 - brick2.y1) -
              (brick1.y2 - brick2.y1)*(brick2.x2 - brick2.x1))
        if (f3 *f4 <= 0) and (g1*g2 <= 0):
            return True

Puzzle = Space('Day22/Example.txt')
a=1