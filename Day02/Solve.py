
class Game:
    def __init__(self, line : str):
        [gameIDstring, gameString] = line.split(':')
        self.ID = int(gameIDstring.replace('Game ', ''))
        hands = gameString.split(';')
        self.hands = []
        for hand in hands:
            RGB = [0,0,0]
            for color in hand.split(','):
                idx = color.find('blue')
                if idx != -1:
                    RGB[2] = int(color.replace('blue', ''))
                idx = color.find('red')
                if idx != -1:
                    RGB[0] = int(color.replace('red', ''))
                idx = color.find('green')
                if idx != -1:
                    RGB[1] = int(color.replace('green', ''))
            self.hands.append(RGB)
            
    def isPossible(self, nbMaxRed, nbMaxGreen, nbMaxBlue):
        for hand in self.hands:
            if hand[0] > nbMaxRed or hand[1] > nbMaxGreen or hand[2] > nbMaxBlue:
                return False
        return True
    
    def power(self):
        redList = []
        greenList = []
        blueList = []
        for hand in self.hands:
            redList.append(hand[0])
            greenList.append(hand[1])
            blueList.append(hand[2])
        power = max(redList) * max(greenList) * max(blueList)
        return power
        
with open('Day02/Input.txt') as file:
    Games = [Game(line) for line in file.readlines()]

sumID = 0
for game in Games:
    if game.isPossible(12, 13, 14):
        sumID += game.ID
        
print(f'Part 1 : Sum of all possibl IDs is {sumID}')

sumPower = 0
for game in Games:
    sumPower += game.power()
        
print(f'Part 2 : Sum of all possibl IDs is {sumPower}')
        