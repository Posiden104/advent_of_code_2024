from Helpers import *
from functools import reduce, cache

@cache
def factors(n):
    return set(reduce(
        list.__add__,
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))



def part1():
    total_cost = 0
    for machine in machines:
        ax, ay, bx, by, px, py = machine
        max_a_x = px // ax
        max_a_y = py // ay
        max_b_x = px // bx
        max_b_y = py // by

        max_a = min(max_a_x, max_a_y)
        max_b = min(max_b_x, max_b_y)


        min_cost = None

        for press_a in range(max_a + 1):
            for press_b in range(max_b + 1, 0, -1):
                cost = press_a * acost + press_b * bcost
                if min_cost != None:
                    continue
                if press_a * ax + press_b * bx == px and press_a * ay + press_b * by == py:
                    # print(f"Press A: {press_a}, Press B: {press_b}")
                    # print(f"this works, cost {cost}")
                    min_cost = min(min_cost, cost) if min_cost != None else cost
        total_cost += min_cost or 0
        # print(f"Min cost for {machine} is {min_cost}")
    return total_cost

def part2():
    pass

example = False
input = read_input(13, example, False)

machines = []

for i in range(0, len(input), 4):
    sp = input[i].split()
    ax = sp[2][2:-1]
    ay = sp[3][2:]
    sp = input[i+1].split()
    bx = sp[2][2:-1]
    by = sp[3][2:]
    sp = input[i+2].split()
    px = sp[1][2:-1]
    py = sp[2][2:]
    machines.append((int(ax), int(ay), int(bx), int(by), int(px), int(py)))

acost = 3
bcost = 1

execute(part1, "Day 13 - Part 1" + (" - Example" if example else ""))
'''
Result: 29187
Operation took 3.689152 sec.
'''

# execute(part2, "Day 13 - Part 2" + (" - Example" if example else ""))
'''
Result: 0
Operation took 0 ms.
'''
