from operator import itemgetter, attrgetter

cardToPower = {'2' : 1, '3' : 2, '4' : 3, '5' : 4, '6' : 5, '7' : 6,
               '8' : 7, '9' : 8, 'T' : 9, 'J' : 10, 'Q' : 11, 'K' : 12, 'A' : 13}

cardToPowerP2 = {'2' : 1, '3' : 2, '4' : 3, '5' : 4, '6' : 5, '7' : 6,
               '8' : 7, '9' : 8, 'T' : 9, 'J' : 0, 'Q' : 11, 'K' : 12, 'A' : 13}

handToPower = {'NoPower' : 0, 'Pair' : 1, 'TwoPairs' : 2, 'ThreeOfAKind' : 3,
               'FullHouse' : 4, 'FourOfAKind' : 5, 'FiveOfAKind' : 6}

class Hand:
    def __init__(self, strHand) -> None:
        strCards, strBid = strHand.split(' ')
        self.cards = strCards
        self.bid = int(strBid)

        self.cardCount = dict()
        for card in self.cards:
            self.cardCount[card] = self.cards.count(card)
    
    def detectHandValue(self):
        self.powerType = ''
        bestValue = max(self.cardCount.values())
        if bestValue == 5:
            self.powerType = 'FiveOfAKind'
        elif bestValue == 4:
            self.powerType = 'FourOfAKind'
        elif bestValue == 3:
            if len(self.cardCount) == 2:
                self.powerType = 'FullHouse'
            elif len(self.cardCount) == 3:
                self.powerType = 'ThreeOfAKind'
        elif bestValue == 2:
            if len(self.cardCount) == 4:
                self.powerType = 'Pair'
            else:
                self.powerType = 'TwoPairs'
        if self.powerType == '':
            self.powerType = 'NoPower'

        self.powerType = handToPower[self.powerType]
        self.cardPower0 = cardToPower[self.cards[0]]
        self.cardPower1 = cardToPower[self.cards[1]]
        self.cardPower2 = cardToPower[self.cards[2]]
        self.cardPower3 = cardToPower[self.cards[3]]
        self.cardPower4 = cardToPower[self.cards[4]]

    def detectHandValue_P2(self):
        self.powerType = ''
        countJ = 0
        if 'J' in self.cardCount.keys():
            countJ = self.cardCount.pop('J')
        if countJ == 5:
            bestValue = 5
        else:
            bestValue = max(self.cardCount.values()) + countJ
        if bestValue == 5:
            self.powerType = 'FiveOfAKind'
        elif bestValue == 4:
            self.powerType = 'FourOfAKind'
        elif bestValue == 3:
            if len(self.cardCount) == 2:
                self.powerType = 'FullHouse'
            elif len(self.cardCount) == 3:
                self.powerType = 'ThreeOfAKind'
        elif bestValue == 2:
            if len(self.cardCount) == 4:
                self.powerType = 'Pair'
            elif len(self.cardCount) == 3:
                self.powerType = 'TwoPairs'
        if self.powerType == '':
            self.powerType = 'NoPower'

        self.powerType = handToPower[self.powerType]
        self.cardPower0 = cardToPowerP2[self.cards[0]]
        self.cardPower1 = cardToPowerP2[self.cards[1]]
        self.cardPower2 = cardToPowerP2[self.cards[2]]
        self.cardPower3 = cardToPowerP2[self.cards[3]]
        self.cardPower4 = cardToPowerP2[self.cards[4]]

Hands = []
with open("Day07/Input.txt") as file:
    Hands = [Hand(line.strip()) for line in file.readlines()]

Hands_Basic = Hands
for hand in Hands_Basic:
    hand.detectHandValue()

Hands_Basic = sorted(Hands_Basic, key=attrgetter('powerType',
                                     'cardPower0', 'cardPower1',
                                     'cardPower2', 'cardPower3', 'cardPower4'))

totalBid = 0
for idx, hand in enumerate(Hands_Basic):
    totalBid += hand.bid * (idx + 1)

print(f'Part 1 : Total Bid is {totalBid}')

Hands_Next = Hands
for hand in Hands_Next:
    hand.detectHandValue_P2()

Hands_Next = sorted(Hands_Next, key=attrgetter('powerType',
                                     'cardPower0', 'cardPower1',
                                     'cardPower2', 'cardPower3', 'cardPower4'))

totalBid = 0
for idx, hand in enumerate(Hands_Next):
    totalBid += hand.bid * (idx + 1)

print(f'Part 2 : Total Bid is {totalBid}')

