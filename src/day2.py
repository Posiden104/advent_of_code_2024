# Part 1

with open('src/input/day2_input.txt', 'r') as file:
    reports = file.readlines()

safe_reports = 0
unsafe_reports = 0

for report in reports:
    levels = list(map(int, report.split(' ')))
    solved = False

    # duplicates
    for level in levels:
        if levels.count(level) > 1:
            unsafe_reports += 1
            solved = True
            break

    if solved:
        continue

    # increasing or decreasing
    if levels[0] < levels [1]:
        # increasing
        for level in levels:
            if levels.index(level) == len(levels) - 1:
                break
            next = levels[levels.index(level) + 1]
            if level > next or next - level > 3:
                unsafe_reports += 1
                solved = True
                break
    else:
        # decreasing
        for level in levels:
            if levels.index(level) == len(levels) - 1:
                break
            next = levels[levels.index(level) + 1]
            if level < next or level - next > 3:
                unsafe_reports += 1
                solved = True
                break

    if not solved:
        safe_reports += 1

print(f'Safe reports: {safe_reports}')
print(f'Unsafe reports: {unsafe_reports}')
print(f'total reports: {len(reports)}')
print(f'total reports solved: {safe_reports + unsafe_reports}')