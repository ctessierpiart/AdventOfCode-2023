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
    
    def getSym(self):
        isSym = False
        for idx in range(self.len_y-1):
            isSym = self.isEqual(self.getLine(idx), self.getLine(idx+1))
            n=0
            while isSym:
                n += 1
                line1, line2 = self.getLine(idx-n), self.getLine(idx+1+n)
                if (line1 == 0 or line2 == 0):
                    return (idx + 1) * 100
                isSym = self.isEqual(line1, line2)
        
        for idx in range(self.len_x-1):
            isSym = self.isEqual(self.getCol(idx), self.getCol(idx+1))
            n=0
            while isSym:
                n += 1
                line1, line2 = self.getCol(idx-n), self.getCol(idx+1+n)
                if (line1 == 0 or line2 == 0):
                    return (idx + 1)
                isSym = self.isEqual(line1, line2)
        return 0

    def isEqual(self, line1, line2):
        nbDiff = 0
        for char1, char2 in zip(line1, line2):
            if char1 != char2:
                nbDiff += 1
        if nbDiff == 0:
            return True
        return False
    
    def getSymSmudge(self):
        isSym = False
        for idx in range(self.len_y-1):
            line1, line2 = self.getLine(idx), self.getLine(idx+1)
            self.smudged = False
            isSym = self.isEqualSmudge(line1, line2)
            n = 0
            while isSym:
                n += 1
                line1, line2 = self.getLine(idx-n), self.getLine(idx+1+n)
                if (line1 == 0 or line2 == 0):
                    if self.smudged:
                        return (idx + 1)*100
                    else:
                        break
                isSym = self.isEqualSmudge(line1, line2)
        isSym = False
        for idx in range(self.len_x-1):
            line1, line2 = self.getCol(idx), self.getCol(idx+1)
            self.smudged = False
            isSym = self.isEqualSmudge(line1, line2)
            n = 0
            while isSym:
                n += 1
                line1, line2 = self.getCol(idx-n), self.getCol(idx+1+n)
                if (line1 == 0 or line2 == 0):
                    if self.smudged:
                        return (idx + 1)
                    else:
                        break
                isSym = self.isEqualSmudge(line1, line2)
        return 0

    def isEqualSmudge(self, line1, line2):
        nbDiff = 0
        for char1, char2 in zip(line1, line2):
            if char1 != char2:
                nbDiff += 1
        if nbDiff == 0:
            return True
        elif nbDiff == 1 and not self.smudged:
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
    result += mirror.getSym()

print(f'Part 1 : {result}')

result = 0
for mirror in Mirrors:
    result += mirror.getSymSmudge()

print(f'Part 2 : {result}')