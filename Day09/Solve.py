class Parameter:
    def __init__(self, line):
        self.history = [int(number) for number in line.split(' ')]
        
    def extratpolate(self):
        listExtrapolation = [self.history]
        while self.sumabs(listExtrapolation[-1]):
            newExtrapol = []
            for idx in range(1, len(listExtrapolation[-1])):
                val = listExtrapolation[-1][idx] - listExtrapolation[-1][idx-1]
                newExtrapol.append(val)
            listExtrapolation.append(newExtrapol)

        for idx in range(len(listExtrapolation)-1, -1, -1):
            if idx == len(listExtrapolation)-1:
                listExtrapolation[idx].append(0)
                continue
            valeExtrapolation = listExtrapolation[idx][-1] + listExtrapolation[idx+1][-1]
            listExtrapolation[idx].append(valeExtrapolation)
            
        return listExtrapolation[0][-1]
    
    def extratpolateBack(self):
        listExtrapolation = [self.history]
        while sum(map(abs, listExtrapolation[-1])):
            newExtrapol = []
            for idx in range(1, len(listExtrapolation[-1])):
                val = listExtrapolation[-1][idx] - listExtrapolation[-1][idx-1]
                newExtrapol.append(val)
            listExtrapolation.append(newExtrapol)

        for idx in range(len(listExtrapolation)-1, -1, -1):
            if idx == len(listExtrapolation)-1:
                listExtrapolation[idx] = [0] + listExtrapolation[idx]
                continue
            valeExtrapolation = listExtrapolation[idx][0] - listExtrapolation[idx+1][0]
            listExtrapolation[idx] = [valeExtrapolation] + listExtrapolation[idx]
            
        return listExtrapolation[0][0]
                
with open('Day09/Input.txt') as file:
    Parameters = [Parameter(line.strip()) for line in file.readlines()]

sumExtra = sum([param.extrapolate() for param in Parameters])
print(f'Part 1 : {sumExtra}')

sumExtra = sum([param.extratpolateBack() for param in Parameters])
print(f'Part 2 : {sumExtra}')