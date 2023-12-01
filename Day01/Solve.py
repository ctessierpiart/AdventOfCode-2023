with open("Day01/Input.txt") as file:
    calibration_values = [line.strip() for line in file.readlines()]

def decode_art(art : str):
    first_digit = ''
    last_digit = ''
    for char in art:
        if char.isnumeric():
            first_digit = char
            break
    for char in reversed(art):
        if char.isnumeric():
            last_digit = char
            break
    return int(first_digit + last_digit)

calibration = 0
for art in calibration_values:
    calibration += decode_art(art)

print(f'Part 1 : calibration value is {calibration}')

def decode_art_better(art : str):
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9',
            'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    occurences = [art.rfind(num) for num in numbers]
    last_digit_idx = occurences.index(max(occurences))
    occurences = [art.find(num) for num in numbers]
    for idx, occ in enumerate(occurences):
        if occ == -1:
            occurences[idx] = 100
    first_digit_idx = occurences.index(min(occurences))
    if last_digit_idx >= 9:
        last_digit_idx -= 9
    if first_digit_idx >= 9:
        first_digit_idx -= 9
    value = int(str(first_digit_idx+1) + str(last_digit_idx+1))
    print(f'{art} ==> {value}')
    return value

better_calibration = 0
for idx, art in enumerate(calibration_values):
    if idx > 990:
        a = 1
    better_calibration += decode_art_better(art)

print(f'Part 2 : calibration value is {better_calibration}')