from Helpers import *

counted = set()

def area(row, col, crop, pt1=True):
    if row < 0 or row >= height or col < 0 or col >= width:
        return
    area = 0
    perim = 0
    to_check = set()
    u_edges = {}
    d_edges = {}
    l_edges = {}
    r_edges = {}

    counted.add((row, col)) 
    to_check.add((row, col))

    # print(f"Checking: {row}, {col}, Crop: {crop}")
    while len(to_check) > 0:
        r, c = to_check.pop()
        counted.add((r, c))
        area += 1

        up = r - 1 if r - 1 >= 0 else None
        down = r + 1 if r + 1 < height else None
        left = c - 1 if c - 1 >= 0 else None
        right = c + 1 if c + 1 < width else None

        # perim += [up, down, left, right].count(None)
        # if [up, down, left, right].count(None) > 0:
        #     print(f"added {[up, down, left, right].count(None)} to perim for none's")

        if up != None and input[up][c] == crop:
            if (up,c) not in counted:
                # print(f"Adding: {up}, {c}")
                to_check.add((up, c))
        else:
            # print(f"Adding 1 to perim because {up}, {c} = {input[up][c]}")
            perim += 1
            if r in u_edges:
                u_edges[r].append(c)
            else:
                u_edges[r] = [c]
        if down != None and input[down][c] == crop:
            if (down,c) not in counted:
                # print(f"Adding: {down}, {c}")
                to_check.add((down, c))
        else:
            # print(f"Adding 1 to perim because {down}, {c} = {input[down][c]}")
            perim += 1
            if r in d_edges:
                d_edges[r].append(c)
            else:
                d_edges[r] = [c]
        if left != None and input[r][left] == crop:
            if (r,left) not in counted:
                # print(f"Adding: {r}, {left}")
                to_check.add((r, left))
        else:
            # print(f"Adding 1 to perim because {r}, {left} = {input[r][left]}")
            perim += 1
            if c in l_edges:
                l_edges[c].append(r)
            else:
                l_edges[c] = [r]
        if right != None and input[r][right] == crop:
            if (r,right) not in counted:
                # print(f"Adding: {r}, {right}")
                to_check.add((r, right))
        else:
            # print(f"Adding 1 to perim because {r}, {right} = {input[r][right]}")
            perim += 1
            if c in r_edges:
                r_edges[c].append(r)
            else:
                r_edges[c] = [r]
        
    # print(f"Crop: {crop}, Area: {area}, Perimeter: {perim}")
    if pt1:
        return area * perim
    else:
        edges = 0
        for r in u_edges:
            r = sorted(u_edges[r])
            edges += 1
            for i in range(len(r) -1):
                if r[i + 1] - r[i] > 1:
                    edges += 1
        
        for r in d_edges:
            r = sorted(d_edges[r])
            edges += 1
            for i in range(len(r) -1):
                if r[i + 1] - r[i] > 1:
                    edges += 1
        
        for c in l_edges:
            r = sorted(l_edges[c])
            edges += 1
            for i in range(len(r) -1):
                if r[i + 1] - r[i] > 1:
                    edges += 1
        
        for c in r_edges:
            r = sorted(r_edges[c])
            edges += 1
            for i in range(len(r) -1):
                if r[i + 1] - r[i] > 1:
                    edges += 1
        # print(f"Crop {crop} has {edges} edges")
        return area * edges
        


def part1():
    fence_cost = 0
    # print(f'Width: {width}, Height: {height}')
    for r in range(height):
       for c in range(width):
            if (r, c) in counted:
                continue
            else:
                # print(f"Checking: {r}, {c}")
                fence_cost += area(r, c, input[r][c])
    return fence_cost

def part2():
    fence_cost = 0
    print(f'Width: {width}, Height: {height}')
    for r in range(height):
       for c in range(width):
            if (r, c) in counted:
                continue
            else:
                # print(f"Checking: {r}, {c}")
                fence_cost += area(r, c, input[r][c], False)
    return fence_cost

example = False
input = read_input(12, example, False)
width = len(input[0])
height = len(input)

# execute(part1, "Day 12 - Part 1" + (" - Example" if example else ""))
'''
Result: 246336 - too low (🤦 I left in the limit of 20 in there...)
Operation took 228.580400 ms. (Tons of prints too...)
Result: 1424472
Operation took 58.163000 ms.
'''
execute(part2, "Day 12 - Part 2" + (" - Example" if example else ""))
'''
Result: 870202
Operation took 74.878000 ms.
'''
