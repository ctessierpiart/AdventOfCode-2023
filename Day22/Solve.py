class Brick:
    def __init__(self, line, start_z = 0):
        if isinstance(line, str):
            begin_coord_str, end_coord_str = line.split('~')
            self.coord_begin = [int(char) for char in begin_coord_str.split(',')]
            self.coord_end = [int(char) for char in end_coord_str.split(',')]
        else:
            self.coord_begin = line.coord_begin
            self.coord_end = line.coord
            delta = self.coord_begin[2] - start_z
            self.coord_end[2] -= delta
            self.coord_begin[2] -= delta
        (self.x1, self.y1, self.z1) = self.coord_begin
        (self.x2, self.y2, self.z2) = self.coord_end
        self.contact_above = []
        self.contact_below = []
        self.lowest_point = min(self.z1, self.z2)
        self.highest_point = max(self.z1, self.z2)

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
            for settled_brick in reversed(self.settle):
                if self.check_overlap(brick, settled_brick):
                    new_brick = Brick(brick, settled_brick.highest_point)
                

    def get_brick(self, idx):
        if idx < 0 or idx >= self.len:
            return None
        return self.bricks[idx]

    def check_overlap(self, brick1, brick2):
        if ((brick1.x1 in range(brick2.x1, brick2.x2+1) and 
            brick1.y2 in range(brick2.y1, brick2.y2+1)) or
            (brick1.y1 in range(brick2.y1, brick2.y2+1) and 
            brick1.x2 in range(brick2.x1, brick2.x2+1))):
            return True
        return False

Puzzle = Space('Day22/Example.txt')
a=1