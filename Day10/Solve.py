class Node:
    def __init__(self, nodeType : str, coord : tuple):
        self.coord = coord
        self.nodeType = nodeType
        self.links = []
        (x, y) = coord
        if nodeType == '|':
            self.links = [(x, y+1), (x, y-1)]
        elif nodeType == '-':
            self.links = [(x-1, y), (x+1, y)]
        elif nodeType == 'L':
            self.links = [(x, y-1), (x+1, y)]
        elif nodeType == '7':
            self.links = [(x-1, y), (x, y+1)]
        elif nodeType == 'J':
            self.links = [(x, y-1), (x-1, y)]
        elif nodeType == 'F':
            self.links = [(x, y+1), (x+1, y)]
        elif nodeType == '.':
            self.links = []
        elif nodeType == 'S':
            self.links = []
        
        
    def nextNode(self, start : tuple):
        if self.links.index(start) == 1:
            return self.links[0]
        else:
            return self.links[1]
        

class LoopMap:
    def __init__(self, fileLocation):
        self.Nodes = []
        with open(fileLocation) as file:
            for lineIdx, line in enumerate(file.readlines()):
                lineNodes = []
                for charIdx, char in enumerate(line.strip()):
                    lineNodes.append(Node(char, (charIdx, lineIdx)))
                self.Nodes.append(lineNodes)
        
        for line in self.Nodes:
            for node in line:
                if node.nodeType == 'S':
                    self.startNode = node
                    (xStart, yStart) = node.coord
                    type = '.'
                    upNode = self.map((xStart, yStart-1))
                    downNode = self.map((xStart, yStart+1))
                    leftNode = self.map((xStart-1, yStart))
                    rightNode = self.map((xStart+1, yStart))
                    if node.coord in upNode.links and node.coord in downNode.links:
                        type = '|'
                    elif node.coord in leftNode.links and node.coord in rightNode.links:
                        type = '-'
                    elif node.coord in upNode.links and node.coord in leftNode.links:
                        type = 'J'
                    elif node.coord in downNode.links and node.coord in rightNode.links:
                        type = 'F'
                    elif node.coord in leftNode.links and node.coord in downNode.links:
                        type = '7'
                    elif node.coord in rightNode.links and node.coord in upNode.links:
                        type = 'L'
                    self.Nodes[yStart][xStart] = Node(type, (xStart, yStart))
                    self.startNode = Node(type, (xStart, yStart))
                    break
    
    def map(self, coord : tuple):
        if coord[0] >= len(self.Nodes[0]) or coord[0] < 0:
            return 0
        if coord[1] >= len(self.Nodes) or coord[1] < 0:
            return 0
        return self.Nodes[coord[1]][coord[0]]
    
    def findFarthest(self):
        (linkCoord, _) = self.startNode.links
        link = self.map(linkCoord)
        last = self.startNode
        nbstep = 1
        while link.coord != self.startNode.coord:
            nbstep += 1
            nextCoord = link.nextNode(last.coord)
            next = self.map(nextCoord)
            last = link
            link = next
        return nbstep
    
    def scanNeighbours(self, node, previousNode):
        nodeCoord = node.coord
        upNode =     self.map((nodeCoord[0],     nodeCoord[1] - 1))
        downNode =   self.map((nodeCoord[0],     nodeCoord[1] + 1))
        leftNode =   self.map((nodeCoord[0] - 1, nodeCoord[1]))
        rightNode =  self.map((nodeCoord[0] + 1, nodeCoord[1]))
        
        for node in [upNode, downNode, rightNode, leftNode]:
            if node == 0:
                continue
            if node.nodeType != 'X':
    
    def areaInsideLoop(self):
        (linkCoord, _) = self.startNode.links
        link = self.map(linkCoord)
        last = self.startNode 
        while link.coord != self.startNode.coord:
            link.nodeType = 'X'
            nextCoord = link.nextNode(last.coord)
            next = self.map(nextCoord)
            last = link
            link = next
            
        (linkCoord, _) = self.startNode.links
        link = self.map(linkCoord)
        last = self.startNode
        while link.coord != self.startNode.coord:
            
            
            nextCoord = link.nextNode(last.coord)
            next = self.map(nextCoord)
            last = link
            link = next
                
Map = LoopMap('Day10/Input.txt')

dist = Map.findFarthest()
print(f'Part 1 : {dist//2}')