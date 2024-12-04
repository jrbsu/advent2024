import re

def recursive_items(dictionary):
    for key, value in dictionary.items():
        if type(value) is dict:
            yield from recursive_items(value)
        else:
            yield (key, value)

with open('input.txt', 'r') as file:
    lines = file.readlines()

number_pairs = {}

for index, line in enumerate(lines):
    numbers = re.match(r'(\d{5})\s+(\d{5})', line)
    number_pairs[index] = {'left': int(numbers.group(1)), 'right': int(numbers.group(2))}

left = []
right = []

for key, value in recursive_items(number_pairs):
    if key == 'left':
        left.append(value)
    elif key == 'right':
        right.append(value)
    else:
        print(f'WARNING: Invalid key {key}')

# PART ONE
left_part_one = left.copy()
right_part_one = right.copy()
total_diff = 0

for index in range(len(left_part_one)):
    min_left = min(left_part_one)
    min_right = min(right_part_one)
    diff = min_left - min_right
    if diff < 0:
        diff = diff * -1
    left_part_one.remove(min_left)
    right_part_one.remove(min_right)
    total_diff += diff

print(f'Part one answer: {total_diff}')

# PART TWO
total_score = 0

for number in left:
    score = number * right.count(number)
    total_score += score

print(f'Part two answer: {total_score}')