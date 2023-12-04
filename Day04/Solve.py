class Card:
    def __init__(self, cardString):
        [cardIDstring, numbersString] = cardString.split(':')
        self.ID = int(cardIDstring.replace('Card', ''))
        [winningString, numbersString] = numbersString.split('|')
        self.winningNumbers = []
        winningString = winningString.split(' ')
        for number in winningString:
            if number.isnumeric():
                self.winningNumbers.append(int(number))
                
        self.playNumbers = []
        numbersString = numbersString.split(' ')
        for number in numbersString:
            if number.isnumeric():
                self.playNumbers.append(int(number))
                
    def calcWorth(self):
        self.amountWinning = 0
        self.worth = 0
        for number in self.playNumbers:
            if number in self.winningNumbers:
                self.amountWinning += 1
                if self.worth == 0:
                    self.worth = 1
                else:
                    self.worth *= 2
        
        return self.worth

with open('Day04/Input.txt') as file:
    Cards = [Card(line.strip()) for line in file.readlines()]
    
totalWorth = 0
for card in Cards:
    totalWorth += card.calcWorth()
    
print(f'Part 1 : Total worth of cards is {totalWorth}')

#Not necessary but it makes this part independant from part 1
for card in Cards:
    card.calcWorth()

cardAmount = [1 for i in range(len(Cards))]
for idx, card in enumerate(Cards):
    for iteration in range(cardAmount[idx]):
        totalWorth += card.worth
        for i in range(idx+1, idx+1+card.amountWinning):
            cardAmount[i] += 1

totalCard = sum(cardAmount)
print(f'Part 2 : Total worth of cards is {totalCard}')