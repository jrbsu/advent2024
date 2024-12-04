import re

with open('input.txt', 'r') as file:
    data = file.read()

def get_total(data):
    return sum(
        int(a) * int(b)
        for a, b in re.findall(r'mul\((\d+),(\d+)\)', data)
    )

def part_one():
    print(f'Part one answer: {get_total(data)}')

def part_two():
    split_data = re.split(r'(do\(\)|don\'t\(\))', data)
    enabled = True
    total = 0
    for element in split_data:
        if element == "don\'t()":
            enabled = False
        elif element == "do()":
            enabled = True
        elif enabled:
            total += get_total(element)
            
    print(f'Part two answer: {total}')

part_one()
part_two()