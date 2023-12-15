class Step_hash:
    def __init__(self, step_str):
        self.data = step_str
        self.value = 0
        self.operation = None 
        self.name = ''
        for char in self.data:
            if self.operation != None:
                self.focal_length = int(char)
            elif char == '=' or char == '-':
                self.operation = char
                self.step_value = self.value
            else:
                 self.name += char
            self.value += ord(char)
            self.value *= 17
            self.value %= 256

class Box:
    def __init__(self, box_number):
        self.box_number = box_number
        self.lenses_names = []
        self.lenses_value = {}

    def process_step(self, step):
        if step.operation == '=':
            if step.name not in self.lenses_names:
                self.lenses_names.append(step.name)
                self.lenses_value[step.name] = step.focal_length
            else:
                self.lenses_value[step.name] = step.focal_length
        else:
            if step.name in self.lenses_names:
                self.lenses_names.remove(step.name)

    def get_focal_power(self):
        value = 0
        for idx, lens in enumerate(self.lenses_names):
            value += self.lenses_value[lens] * (idx + 1) * (self.box_number + 1)
        return value 


with open('Day15/Input.txt') as file:
        strToConvert = file.readline().strip().split(',')
        Hash_list = [Step_hash(step_string) for step_string in strToConvert]

print(f'Part 1 : {sum([step.value for step in Hash_list])}')

Boxes = {}
for step in Hash_list:
    if step.step_value not in Boxes.keys():
        Boxes[step.step_value] = Box(step.step_value)
    Boxes[step.step_value].process_step(step)

value = 0
for box in Boxes.values():
    value += box.get_focal_power()
print(f'Part 2 : {value}')