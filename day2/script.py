def is_monotonic(data_line):
    return all(i < j for i, j in zip(data_line, data_line[1:])) or all(i > j for i, j in zip(data_line, data_line[1:]))

def is_valid_difference(pair):
    return 1 <= abs(pair[0] - pair[1]) <= 3

def check_datapoint(points):
    check = True if abs(points[0] - points[1]) >= 1 and abs(points[0] - points[1]) <= 3 else False
    return check

def check_full_line(data_line):
    for i in range(len(data_line) - 1):
        if not is_valid_difference((data_line[i], data_line[i + 1])):
            return 0
    return 1

with open('input.txt', 'r') as file:
    lines = file.readlines()

def part_one():
    total_safe = 0

    for line in lines:
        data_line = [int(x) for x in line.strip().split()]

        # Immediately end if the list isn't always increasing or decreasing
        if not is_monotonic(data_line):
            continue

        total_safe += check_full_line(data_line)

    print(total_safe)

def part_two():
    total_safe = 0

    for line in lines:
        data_line = [int(x) for x in line.strip().split()]

        new_lists = []
        safe_lists = []

        # Make a list of lists with one element removed from each
        for y in range(len(data_line)):
            new_list = data_line[:]
            new_list.pop(y)
            new_lists.append(new_list)

        for list in new_lists:
            # Immediately end if the list isn't always increasing or decreasing
            if not is_monotonic(list):
                continue

            safe_lists.append(check_full_line(list))

        if safe_lists.count(1) > 0:
            total_safe += 1

    print(total_safe)

part_two()