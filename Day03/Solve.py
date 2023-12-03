class NumberSch:
    def __init__(self, number : str, start_coord : list):
        self.number = int(number)
        self.start_coord = start_coord
        self.end_coord = [start_coord[0]+len(number), start_coord[1]]
        
    def isEnginePart(self, listSymbol : list):
        for symbol in listSymbol:
            if abs(symbol.coord[1] - self.start_coord[1]) <= 1:
                for idx in range(self.start_coord[0], self.end_coord[0]):
                    if abs(idx - symbol.coord[0]) <= 1:
                        return True
        return False
            
            
        
class SymbolSch:
    def __init__(self, symbol : str, coord : str):
        self.symbol = symbol
        self.coord = coord
        
    def gearPower(self, listNumber):
        if self.symbol == '*':
            adjacent_numbers = []
            for number in listNumber:
                if abs(number.start_coord[1] - self.coord[1]) <= 1:
                    for idx in range(number.start_coord[0], number.end_coord[0]):
                        if abs(idx - self.coord[0]) <= 1:
                            adjacent_numbers.append(number)
                            break
            if len(adjacent_numbers) == 2:
                return adjacent_numbers[0].number * adjacent_numbers[1].number
            else:
                return 0
        return 0
            

listNumber = []
listSymbol = []

char_state = 'waitForElement'
with open('Day03/Input.txt') as file:
    for line_idx, line in enumerate(file.readlines()):
        if char_state == 'isNumber':
            listNumber.append(NumberSch(element_string, coord))
        char_state = 'waitForElement'
        for char_idx, char in enumerate(line.strip()):
            if char_state == 'waitForElement':
                if char.isnumeric():
                    char_state = 'isNumber'
                    element_string = char
                    coord = [char_idx, line_idx]
                elif char != '.':
                    element_string = char
                    coord = [char_idx, line_idx]
                    listSymbol.append(SymbolSch(char, coord))
            elif char_state == 'isNumber':
                if char.isnumeric():
                    element_string += char
                else:
                    if char != '.':
                        listSymbol.append(SymbolSch(char, [char_idx, line_idx]))
                    listNumber.append(NumberSch(element_string, coord))
                    char_state = 'waitForElement'

EngineParts = 0
for number in listNumber:
    if number.isEnginePart(listSymbol):
        EngineParts += number.number
        
print(f'Part 1 : Engine power is {EngineParts}')

gearPower = 0
for symbol in listSymbol:
    gearPower += symbol.gearPower(listNumber)
    
print(f'Part 2 : gear Power is {gearPower}')