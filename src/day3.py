import re

# Part 1

with open('src/input/day3_input.txt', 'r') as file:
    reports = file.readlines()

pairs = []
finalVal = 0

for report in reports:
    # pattern = re.compile(r'mul\(\d{1,3},\d{1,3}\)')
    pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')

    matches = pattern.findall(report)

    for match in matches:
        pairs.append([int(match[0]), int(match[1])])
        finalVal += int(match[0]) * int(match[1])
# print(pairs)
print(finalVal)

# Output: 178794710