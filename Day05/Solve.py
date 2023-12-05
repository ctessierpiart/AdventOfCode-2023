class conversionMap:
    def __init__(self, ID, map : list):
        self.ID = ID
        self.map = map

    def findNext(self, attribute):
        for map in self.map:
            if attribute in range(map[1], map[1] + map[2]):
                return map[0] + (attribute - map[1])
        return attribute
    
    def findPrevious(self, attribute):
        for map in self.map:
            if attribute in range(map[0], map[0] + map[2]):
                return map[1] + (attribute - map[0])
        return attribute

def findLocation(seed, maps):
    attribute = seed
    for conversionmap in maps:
        attribute = conversionmap.findNext(attribute)
    return attribute

def findSeed(location, maps):
    attribute = location
    for conversionmap in reversed(maps):
        attribute = conversionmap.findPrevious(attribute)
    return attribute
        
maps = []
Seeds = []
with open('Day05/Input.txt') as file:
    listSeeds = file.readline().strip().split(' ')
    listSeeds = listSeeds[1:]
    Seeds = [(int(element)) for element in listSeeds]
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
    StSMap = conversionMap('Seed To Soil', StS)
    StFMap = conversionMap('Soil To Fert', StF)
    FtWMap = conversionMap('Fert To Wate', FtW)
    WtLMap = conversionMap('Wate To Ligh', WtL)
    LtTMap = conversionMap('Ligh To Temp', LtT)
    TtHMap = conversionMap('Temp to Hume', TtH)
    HtLMap = conversionMap('Hume to Loca', HtL)
    maps = [StSMap, StFMap, FtWMap, WtLMap, LtTMap, TtHMap, HtLMap]

locations = [findLocation(seed, maps) for seed in Seeds]

print(f'Part 1 : the lowest location is {min(locations)}')

seedRanges = [[Seeds[idx], Seeds[idx+1]] for idx in range(0, len(Seeds), 2)]

currentLocation = 0
stepLocation = 1000000
currentSeed = 0
while(stepLocation != 0):
    seedFound = False
    currentLocation += stepLocation
    currentSeed = findSeed(currentLocation, maps)
    for seedRange in seedRanges:
        if currentSeed in range(seedRange[0], seedRange[0] + seedRange[1]):
            seedFound = True
    if seedFound:
        if stepLocation == 1:
            break
        currentLocation -= stepLocation
        stepLocation //= 10
        currentLocation -= stepLocation

print(f'Part 2 : Lowest seed {currentSeed}')