import re
import itertools

class Spring:
    def __init__(self, line):
        [self.spring, numberString] = line.strip().split(' ')
        self.counts = [int(char) for char in numberString.split(',')]

    def calcPossibilties(self):
        nbBit = self.spring.count('?')
        nbTestDamaged = sum(self.counts) - self.spring.count('#')
        nbPos = 0
        for bitIter in bitGenerate(nbBit):
            if bitIter.count('1') != nbTestDamaged:
                continue
            testString = self.springTry(bitIter)
            damagedGroups = re.findall('#+', testString)
            damagedGroups = [len(group) for group in damagedGroups]
            if damagedGroups == self.counts:
                nbPos += 1

        return nbPos

    def springTry(self, stringToTest : set):
        returnString = ''
        idx = 0
        for char in self.spring:
            if char == '?':
                if  stringToTest[idx] == '0':
                    returnString += '.'
                else:
                    returnString += '#'
                idx += 1
                continue
            returnString += char

        return returnString

def bitGenerate(n, minValue = 0):
    for i in range(minValue, 2**n):
        yield '{:0{n}b}'.format(i, n=n)

Springs = []
with open('Day12/Input.txt') as file:
    Springs = [Spring(line.strip()) for line in file.readlines()]

nbPos = 0
for spring in Springs:
    nbPos += spring.calcPossibilties()
print(f'Part 1 : {nbPos}')

bigSpring = []
for spring in Springs:
    spring.spring = spring.spring*5
    spring.counts = spring.counts*5
    bigSpring.append(spring)

nbPos = 0
for spring in bigSpring:
    nbPos += spring.calcPossibilties()
print(f'Part 2 : {nbPos}')

