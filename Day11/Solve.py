Map = []
class Galaxy:
    def __init__(self, coord : tuple):
        self.coord = coord
        self.x = coord[0]
        self.y = coord[1]

def findGaps(axis, dictGlaxy):
    if axis == 'x':
        listPos =  [galaxy.x for galaxy in dictGlaxy.values()]
    else:
        listPos =  [galaxy.y for galaxy in dictGlaxy.values()]
    listVoid = []
    for idx in range(max(listPos)):
        if idx in listPos:
            continue
        listVoid.append(idx)
    return listVoid 

def timeDilation(listVoidX, listVoidY, galaxy, time):
    Xcount, Ycount = 0, 0
    for X in listVoidX:
        if galaxy.x < X:
            break
        Xcount += 1
    galaxy.x += Xcount*time
    for Y in listVoidY:
        if galaxy.y < Y:
            break
        Ycount += 1
    galaxy.y += Ycount*time

def measureDist(node1, node2):
    return abs(node1.x - node2.x) + abs(node1.y - node2.y)

Galaxies = {}
galaxyCount = 0
with open('Day11/Input.txt') as file:
    for idxLine, line in enumerate(file.readlines()):
        for idxChar, char in enumerate(line.strip()):
            if char == '#':
                Galaxies[str(galaxyCount)] = Galaxy((idxChar, idxLine))
                galaxyCount += 1

listVoidX = findGaps('x', Galaxies)
listVoidY = findGaps('y', Galaxies)

#Part 1 : 2; Part 2 : 1000000
dilation = 1000000
for galaxy in Galaxies.values():
    timeDilation(listVoidX, listVoidY, galaxy,dilation -1)

Pair_dist = {}
for galaxy_key, galaxy in Galaxies.items():
    for pair_key, pair in Galaxies.items():
        if galaxy_key + '-' + pair_key in Pair_dist.keys() or pair_key + '-' + galaxy_key in Pair_dist.keys():
            continue
        Pair_dist[galaxy_key + '-' + pair_key] = measureDist(galaxy, pair)

sumDist = sum([dist for dist in Pair_dist.values()])
print(f'Dist : {sumDist}')