def check_saftey(report):
    levels = list(map(int, report.split(' ')))

    # duplicates
    for level in levels:
        if levels.count(level) > 1:
            # print(f'{report} unsafe due to Duplicate level: {level}')
            return False

    # increasing or decreasing
    if levels[0] < levels [1]:
        # increasing
        for level in levels:
            if levels.index(level) == len(levels) - 1:
                break
            next = levels[levels.index(level) + 1]
            if level > next or next - level > 3:
                # print(f'increasing report {report} unsafe due to level: {level} and next: {next}')
                return False
    else:
        # decreasing
        for level in levels:
            if levels.index(level) == len(levels) - 1:
                break
            next = levels[levels.index(level) + 1]
            if level < next or level - next > 3:
                # print(f'decreasing report {report} unsafe due to level: {level} and next: {next}')
                return False

    return True

# Part 1

with open('src/input/day2_input.txt', 'r') as file:
    reports = file.readlines()

safe_reports = []
unsafe_reports = []

for report in reports:
    if check_saftey(report):
        safe_reports.append(report)
    else:
        unsafe_reports.append(report)
    

print(f'Safe reports: {len(safe_reports)}')
print(f'Unsafe reports: {len(unsafe_reports)}')
print(f'total reports: {len(reports)}')
print(f'total reports solved: {len(safe_reports) + len(unsafe_reports)}')

# Part 2

print("====================")

newly_safe = []

for report in unsafe_reports:
    levels = list(map(int, report.split(' ')))
    for i in range(len(levels)):
        removed = levels.copy()[:i] + levels.copy()[i+1:]
        if check_saftey(' '.join(str(x) for x in removed)):
            print(f'Unsafe report: {report} can be made safe by removing {levels[i]}')
            safe_reports.append(report)
            newly_safe.append(report)
            break

for report in newly_safe:
    unsafe_reports.remove(report)

print("====================")

print(f'New Count of Safe reports: {len(safe_reports)}')
print(f'Still Unsafe reports: {len(unsafe_reports)}')
print(f'total reports: {len(reports)}')
print(f'total reports solved: {len(safe_reports) + len(unsafe_reports)}')