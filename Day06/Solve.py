import math
import re

class Race:
    def __init__(self, time, record):
        self.time = time
        self.record = record

    def holdTimes(self):
        #Nice polynomial !!
        sqrtdelta = math.sqrt(self.time*self.time - 4*self.record)
        self.tHoldmin = math.ceil(0.5*(self.time - sqrtdelta))
        self.tHoldmax = math.floor(0.5*(self.time + sqrtdelta))
        #Don't forget to add the TWO values
        return self.tHoldmax - self.tHoldmin + 1
    
Races = []
with open('Day06/Input.txt') as file:
    times = re.findall('\d+', file.readline())
    records = re.findall('\d+', file.readline())
    for time, record in zip(times, records):
        Races.append(Race(int(time), int(record)))
    UniqueRace = Race(int(''.join(times)), int(''.join(records)))

result = 1
for race in Races:
    result *= race.holdTimes()

print(f'Part 1 : The result is {result}')

print(f'Part 2 : result is {UniqueRace.holdTimes()}')