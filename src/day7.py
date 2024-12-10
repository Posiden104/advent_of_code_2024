from concurrent.futures import ThreadPoolExecutor, as_completed
from Helpers import *

operands = ['+', '*']

def solvable(ops, target):
    # print(ops)
    full = (1 << len(ops)-1) - 1
    now = 0
    while now <= full:
        total = ops[0]
        # print(bin(now))
        test = now
        for n in ops[1:]:
            # print(f"{total} {operands[test & 1]} {n}")
            if test & 1:
                total = total * n
            else:
                total = total + n
            test >>= 1
        # print(f"testing {total} == {target}")
        if total == target:
            # print("solution found")
            return True
        now += 1
    # print(bin(full))
    # print("============")
    return False

def part1():
    solution = 0
    for line in input:
        splits = line.strip().split(": ")
        target = int(splits[0])
        ops = [int(x) for x in splits[1].split(" ")]
        
        if solvable(ops, target):
            solution += target
        
    return solution

def part2():
    pass

# example = True
example = False
input = read_input(7, example, False)

execute(part1, "Day 7 - Part 1" + (" - Example" if example else ""))
# Output: 8401132154762 - 545.927200 ms
execute(part2, "Day 7 - Part 2" + (" - Example" if example else ""))
# Output: 0 - 0.00 ms
