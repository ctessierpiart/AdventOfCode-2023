class Seed:
    def __init__(self, ID):
        self.ID = ID
        self.soil = -1
        self.fert = -1
        self.water = -1
        self.light = -1
        self.temp = -1
        self.hum = -1
        self.location = -1

    def findLocation(self, maps):
        self.soil = self._findeq(self.ID, maps[0])
        self.fert = self._findeq(self.soil, maps[1])
        self.water = self._findeq(self.fert, maps[2])
        self.light = self._findeq(self.water, maps[3])
        self.temp = self._findeq(self.light, maps[4])
        self.hum = self._findeq(self.temp, maps[5])
        self.location = self._findeq(self.hum, maps[6])
        return self.location

    def _findeq(self, att, map):
        for conv in map:
            if att in range(conv[1], conv[1] + conv[2]):
                return conv[0] + (att - conv[1])
        return att 
        
maps = []
with open('Day05/Input.txt') as file:
    listSeeds = file.readline().strip().split(' ')
    listSeeds = listSeeds[1:]
    Seeds = [Seed(int(element)) for element in listSeeds]
    state = ''
    StS, StF, FtW, WtL, LtT, TtH, HtL = [], [], [], [], [], [], []
    for line in file.readlines():
        if line.strip() == 'seed-to-soil map:': state = 'StS'
        elif line.strip() == 'soil-to-fertilizer map:': state = 'StF'
        elif line.strip() == 'fertilizer-to-water map:': state = 'FtW'
        elif line.strip() == 'water-to-light map:': state = 'WtL'
        elif line.strip() == 'light-to-temperature map:': state = 'LtT'
        elif line.strip() == 'temperature-to-humidity map:': state = 'TtH'
        elif line.strip() == 'humidity-to-location map:': state = 'HtL'
        elif line.strip() != '':
            conv = [int(value) for value in line.strip().split()]
            if state == 'StS':
                StS.append(conv)
            elif state == 'StF':
                StF.append(conv)
            elif state == 'FtW':
                FtW.append(conv)
            elif state == 'WtL':
                WtL.append(conv)
            elif state == 'LtT':
                LtT.append(conv)
            elif state == 'TtH':
                TtH.append(conv)
            elif state == 'HtL':
                HtL.append(conv)
    StS.sort(key = lambda elem : elem[1])
    StF.sort(key = lambda elem : elem[1])
    FtW.sort(key = lambda elem : elem[1])
    WtL.sort(key = lambda elem : elem[1])
    LtT.sort(key = lambda elem : elem[1])
    TtH.sort(key = lambda elem : elem[1])
    HtL.sort(key = lambda elem : elem[1])
    maps = [StS, StF, FtW, WtL, LtT, TtH, HtL]

locations = [seed.findLocation(maps) for seed in Seeds]

print(f'Part 1 : the lowest location is {min(locations)}')

Seeds = []
isStart = True
for idx, seed_range in enumerate(listSeeds):
    if isStart:
        isStart = False
        for seedID in range(int(seed_range), int(seed_range)+int(listSeeds[idx+1])):
            Seeds.append(Seed(seedID))
    else:
        isStart = True

minlocation = Seeds[0].findLocation(maps)
for seed in Seeds:
    if seed.findLocation(maps) < minlocation:
        minlocation = seed.location

print(f'Part 2 : the lowest location is {minlocation}')

