import re

class Workflow: 
    def __init__(self, line):
        self.name, processStr = line[:-1].split('{')
        processes = processStr.split(',')
        self.processes = {}
        for idx, process in enumerate(processes):
            if len(process) <= 3:
                self.processes[idx] = {'result' : process, 
                                       'type' : 'last'}
            else:
                opStr, result = process.split(':')
                value, op, ref = opStr[0], opStr[1], opStr[2:]
                self.processes[idx] = {'result' : result, 
                                    'value' : value, 
                                    'op' : op, 
                                    'ref' : int(ref),
                                    'type' : 'operation'}
        self.nbProcess = idx + 1

    def process(self, Piece):
        for idx in range(self.nbProcess):
            process = self.processes[idx]
            if process['type'] == 'last':
                return process['result']
            if process['op'] == '=':
                if Piece.values[process['value']] == process['ref']:
                    return process['result']
            elif process['op'] == '<':
                if Piece.values[process['value']] < process['ref']:
                    return process['result']
            elif process['op'] == '>':
                if Piece.values[process['value']] > process['ref']:
                    return process['result']


class Piece:
    def __init__(self, line):
        values = re.findall(r'\d+', line)
        self.values = {'x' : int(values[0]),
                      'm' : int(values[1]),
                      'a' : int(values[2]),
                      's' : int(values[3])}
        self.state = 'ToProcess'
        self.gearValue = sum([value for value in self.values.values()])
        
    def process(self, workflows):
        self.state = 'in'
        while self.state != 'A' and self.state != 'R':
            current_workflow = workflows[self.state]
            self.state = current_workflow.process(self)
        
        if self.state == 'R':
            self.gearValue = 0

Workflows = {}
Pieces = []
with open('Day19/Input.txt') as file:
    workflow_read = True
    for line in file.readlines():
        if line.strip() == '': 
            workflow_read = False
            continue
        else:
            if workflow_read == True:
                workflow = Workflow(line.strip())
                Workflows[workflow.name] = workflow
            else:
                Pieces.append(Piece(line.strip()))

result = 0
for piece in Pieces:
    piece.process(Workflows)
    result += piece.gearValue
print(f'Part 1 : {result}')
        
