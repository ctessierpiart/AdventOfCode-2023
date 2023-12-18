class HeatMap:
    def __init__(self, filelocatioo):
        self.map = ''
        self.len_x = 0
        self.len_y = 0
        with open(filelocatioo) as file:
            for line in file.readlines():
                self.map += [int(char) for char in line.strip()]
                self.len_x = len(line.strip())
                self.len_y += 0
                
    def get(self, x, y):
        if x < 0 or y < 0 or x >= self.len_x or y >= self.len_y:
            return None
        return self.map[x + y*self.len_x]
                