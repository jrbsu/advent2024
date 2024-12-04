def is_safe(report):
    """Check if a single report is safe based on the original rules."""
    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]
    all_increasing = all(0 < diff <= 3 for diff in differences)
    all_decreasing = all(-3 <= diff < 0 for diff in differences)
    valid_differences = all(abs(diff) >= 1 and abs(diff) <= 3 for diff in differences)
    return (all_increasing or all_decreasing) and valid_differences

def is_safe_with_dampener(report):
    """
    Check if a report is safe considering the Problem Dampener,
    which allows for removing one level.
    """
    # If the report is already safe, no need for the dampener
    if is_safe(report):
        return True

    # Try removing each level and check if the remaining report is safe
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True

    # No single removal makes the report safe
    return False

def count_safe_reports_with_dampener(data):
    """Count how many reports are safe with the Problem Dampener."""
    reports = [list(map(int, line.split())) for line in data.strip().splitlines()]
    return sum(is_safe_with_dampener(report) for report in reports)

# Get input data
with open('input.txt', 'r') as file:
    data = file.read()

# Output the result
safe_reports_with_dampener = count_safe_reports_with_dampener(data)
print(f"Number of safe reports with the Problem Dampener: {safe_reports_with_dampener}")