import re
from collections import Counter

# Read and process file
number_pairs = []

with open('input.txt', 'r') as file:
    for line in file:
        match = re.match(r'(\d{5})\s+(\d{5})', line)
        if match:
            number_pairs.append((int(match.group(1)), int(match.group(2))))

# Separate left and right values
left, right = zip(*number_pairs)

# PART ONE
sorted_left = sorted(left)
sorted_right = sorted(right)
total_diff = sum(abs(l - r) for l, r in zip(sorted_left, sorted_right))

print(f'Part one answer: {total_diff}')

# PART TWO
right_counts = Counter(right)
total_score = sum(number * right_counts[number] for number in left)

print(f'Part two answer: {total_score}')
