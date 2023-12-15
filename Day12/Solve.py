import re
import itertools

class Spring:
    def __init__(self, line):
        [self.spring, numberString] = line.strip().split(' ')
        self.counts = [int(char) for char in numberString.split(',')]
        self.spring = self.spring

    def calcPossibilties(self, specString = None, content = None):
        mysteryString = self.spring
        if specString != None:
            mysteryString = specString
        dashcontent = self.counts
        if content != None:
            dashcontent = content
        nbBit = mysteryString.count('?')
        nbTestDamaged = sum(dashcontent) - mysteryString.count('#')
        prototype = nbTestDamaged*'#' + (nbBit-nbTestDamaged)*'.'
        nbPos = 0
        testedStrings = []
        for bitIter in itertools.permutations(prototype):
            if bitIter in testedStrings:
                continue
            else:
                testedStrings.append(bitIter)
            testString = self.springTry(bitIter, mysteryString)
            if [len(seq) for seq in re.findall('#+', testString)] == dashcontent:
                nbPos += 1

        return nbPos
    
    def calcPosTimesFive(self):
        if self.spring[-1] == '.':
            cmplString = '?'+self.spring
            return self.calcPossibilties()*self.calcPossibilties(cmplString)**4
        else:
            totalString = '?'+self.spring
            totalString *= 5
            totalString = totalString[1:]
            return self.calcPossibilties(totalString, self.counts*5)

    def springTry(self, stringToTest : set, specString = None):
        mysteryString = self.spring
        if specString != None:
            mysteryString = specString
        returnString = ''
        idx = 0
        for char in mysteryString:
            if char == '?':
                returnString += stringToTest[idx]
                idx += 1
                continue
            returnString += char

        return returnString

Springs = []
with open('Day12/Example.txt') as file:
    Springs = [Spring(line.strip()) for line in file.readlines()]

nbPos = 0
for spring in Springs:
    nbPos += spring.calcPossibilties()
print(f'Part 1 : {nbPos}')

nbPos = 0
for spring in Springs:
    nbPos += spring.calcPosTimesFive()
print(f'Part 2 : {nbPos}')
