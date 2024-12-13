from Helpers import *
from functools import reduce, cache
from sympy import symbols, Eq, solve

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


        found = False
        for press_a in range(max_a + 1):
            for press_b in range(max_b + 1, 0, -1):
                # if min_cost != None and cost > min_cost:
                #     continue
                if press_a * ax + press_b * bx == px and press_a * ay + press_b * by == py:
                    # print(f"Press A: {press_a}, Press B: {press_b}")
                    # print(f"this works, cost {cost}")
                    total_cost += press_a * acost + press_b * bcost
                    found = True
                    break
            if found:
                break
    return total_cost

# a * 94 + b * 22 = 8400
# a * 34 + b * 67 = 5400

def part2():
    total_cost = 0
    for machine in machines:
        a, b = symbols('a b')
        ax, ay, bx, by, px, py = machine

        eq1 = Eq(a * ax + b * bx, px)
        eq2 = Eq(a * ay + b * by, py)

        sol_dict = solve((eq1, eq2), (a, b))
        
        if sol_dict[a].is_Integer and sol_dict[b].is_Integer:
            total_cost += (sol_dict[a] * acost + sol_dict[b] * bcost)
    return total_cost

example = False
input = read_input(13, example, False)

machines = []

# factor = 0
factor = 10000000000000

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
    machines.append((int(ax), int(ay), int(bx), int(by), int(px) + factor, int(py) + factor))

acost = 3
bcost = 1

# execute(part1, "Day 13 - Part 1" + (" - Example" if example else ""))
'''
Result: 29187
Operation took 1.703375 sec.
'''

execute(part2, "Day 13 - Part 2" + (" - Example" if example else ""))
'''
Result: 99968222587852
Operation took 6.014625 sec.
'''
