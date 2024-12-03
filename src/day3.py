import re


with open('src/input/day3_input.txt', 'r') as file:
    report = file.read().replace('\n', '')

# Part 1

def part1():
    finalVal = 0
    pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')

    matches = pattern.findall(report)

    for match in matches:
        finalVal += int(match[0]) * int(match[1])
    print(finalVal)

    # Output: 178794710

# Part 2

def part2():
    finalVal = 0
    pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
    parse = []
    pairs = []

    # split to the don't()s
    parts = report.split("don't()")

    #take the first part, as its always a do()
    parse.append(parts[0])
    parts = parts[1:]

    # split the do()s
    dos = [parts.split("do()") for parts in parts]
    for do in dos:
        # rip the first index out, as it's a don't() (split on the dont's)
        do = do[1:]
        for d in do:
            parse.append(d)
    
    for i in range(len(parse)):

        matches = pattern.findall(parse[i])

        for match in matches:
            pairs.append([int(match[0]), int(match[1])])
            finalVal += int(match[0]) * int(match[1])
        
    # print(pairs)
    print(finalVal)

    # Output: 76729637

# part1()


import time
 
# Start the stopwatch

start_time = time.perf_counter()
 
# Code block to measure

part1()
 
# Stop the stopwatch

end_time = time.perf_counter()
 
# Calculate the elapsed time

elapsed_time = end_time - start_time

elapsed_time *= 1000

print(f"Operation took {elapsed_time:.6f} ms.")

 
 # Start the stopwatch

start_time = time.perf_counter()
 
# Code block to measure

part2()
 
# Stop the stopwatch

end_time = time.perf_counter()
 
# Calculate the elapsed time

elapsed_time = end_time - start_time

elapsed_time *= 1000

print(f"Operation took {elapsed_time:.6f} ms.")