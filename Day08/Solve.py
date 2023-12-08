import re
import math

class Direction:
    def __init__(self, line):
        self.directions = line
        self.dirPos = 0
        
    def next(self):
        dirToRetrun = self.directions[self.dirPos]
        self.dirPos += 1
        if self.dirPos >= len(self.directions):
            self.dirPos = 0
        return dirToRetrun
    
    def reset(self):
        self.dirPos = 0
    
class Node:
    def __init__(self, line : str):
        self.node, neightbours = line.split(' = ')
        neightbours = neightbours.replace('(', '')
        neightbours = neightbours.replace(')', '')
        self.left, self.right = neightbours.split(', ')
    
    def nextNode(self, direction):
        dir = direction.next()
        if dir == 'R':
            return self.rightNode
        elif dir == 'L':
            return self.leftNode
        
    def nextNode_dir(self, direction):
        if direction == 'R':
            return self.rightNode
        elif direction == 'L':
            return self.leftNode
        
    def setNodes(self, leftNode, rightNode):
        self.leftNode = leftNode
        self.rightNode = rightNode

with open("Day08/Input.txt") as file:
    Dir = Direction(file.readline().strip('\n'))
    file.readline()
    Nodes = [Node(line.strip()) for line in file.readlines()]
#prep
for node in Nodes:
    for leftNode in Nodes:
        if leftNode.node == node.left:
            leftNodeMem = leftNode
            break
    for rightNode in Nodes:
        if rightNode.node == node.right:
            rightNodeMem = rightNode
            break
    node.setNodes(leftNodeMem, rightNodeMem)
        
def findNode(startNodeName, endNodeName):
    for node in Nodes:
        if re.findall(startNodeName + '$', node.node) != []:
            startNode = node
            
    currentNode = startNode.nextNode(Dir)
    nbStep = 1
    while re.findall(endNodeName + '$', currentNode.node) == []:
        currentNode = currentNode.nextNode(Dir)
        nbStep += 1
        
    return nbStep, currentNode

Dir.reset()
result_1, _ = findNode('AAA', 'ZZZ')
print(f'Part 1 : {result_1}')

startNodes = []
for node in Nodes:
    if re.findall('A' + '$', node.node) != []:
        startNodes.append(node)

dist = []
for node in startNodes : 
    Dir.reset()
    nbStep, _ = findNode(node.node, 'Z')
    dist.append(nbStep)

PGCD = 1
for loopdist in dist:
    PGCD = PGCD*loopdist//math.gcd(PGCD, loopdist)
print(f'Part 2 : {PGCD}')