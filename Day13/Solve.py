class Mirror:
    def __init__(self, mirror_span):
        self.len_y = 0
        self.data = []
        for line in mirror_span:
            self.len_y += 1
            self.len_x = len(line)
            self.data += line

        self.smudged = False

    def getLine(self, n):
        if n >= self.len_y or n < 0:
            return 0
        return ''.join(self.data[n*self.len_x:(n+1)*self.len_x])
    
    def getCol(self, n):
        if n >= self.len_x or n < 0:
            return 0
        col = ''
        for idx in range(self.len_y):
            col += self.data[n + idx*self.len_x]
        return col
    
    def getSym(self, smudge_OK = False):
        isSym = False
        for idx in range(self.len_y-1):
            self.smudged = True
            if self.calcDiff(self.getLine(idx), self.getLine(idx+1), smudge_OK) == False:
                continue
            isSym = True
            n=0
            while isSym:
                n += 1
                line1, line2 = self.getLine(idx-n), self.getLine(idx+1+n)
                if line1 == 0 or line2 == 0:
                    return (idx + 1) * 100
                isSym = self.calcDiff(line1, line2, smudge_OK)
        
        for idx in range(self.len_x-1):
            self.smudged = True
            if self.calcDiff(self.getCol(idx), self.getCol(idx+1), smudge_OK) == False:
                continue
            isSym = True
            n=0
            while isSym:
                n += 1
                line1, line2 = self.getCol(idx-n), self.getCol(idx+1+n)
                if line1 == 0 or line2 == 0:
                    return idx + 1
                isSym = self.calcDiff(line1, line2, smudge_OK)

        return 0

    def calcDiff(self, line1, line2, smudge_OK):
        nbDiff = 0
        for char1, char2 in zip(line1, line2):
            if char1 != char2:
                nbDiff += 1
        if nbDiff == 0:
            return True
        if nbDiff == 1 and smudge_OK and not self.smudged == False:
            self.smudged = True
            return True
        return False



Mirrors = []
with open('Day13/Input.txt') as file:
    mirror = []
    for line in file.readlines():
        if line.strip() == '':
            Mirrors.append(Mirror(mirror))
            mirror = []
            continue
        mirror.append(line.strip())
    Mirrors.append(Mirror(mirror))

result = 0
for mirror in Mirrors:
    result += mirror.getSym(True)

print(f'Part 1 : {result}')
