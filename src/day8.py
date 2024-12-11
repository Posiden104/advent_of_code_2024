from Helpers import *

def find_antinodes_by_freq(freq, locs, forever=False):
    anodes = set()
    for i, a in enumerate(locs):
        for j, b in enumerate(locs, i + 1):
            if a == b:
                continue
            vector = vect(a, b)
            v1 = b[0] + vector[0], b[1] + vector[1]
            while v1[0] >= 0 and v1[0] < len(input) and v1[1] >= 0 and v1[1] < len(input[0]):
                anodes.add(v1)
                v1 = v1[0] + vector[0], v1[1] + vector[1]

            v2 = a[0] - vector[0], a[1] - vector[1]
            while v2[0] >= 0 and v2[0] < len(input) and v2[1] >= 0 and v2[1] < len(input[0]):
                anodes.add(v2)
                v2 = v2[0] - vector[0], v2[1] - vector[1]
            anodes.add(a)
            anodes.add(b)
        # for i, r in enumerate(input):
        #     for j, c in enumerate(r):
        #         print(input[i][j] if (i, j) not in anodes else '#', end='')
        #     print()
    return anodes

    
def vect(c1, c2):
    x1, y1 = c1
    x2, y2 = c2
    return ((x2 - x1), (y2 - y1))

def find_antennas():
    antennas = {}
    for i, r in enumerate(input):
        for j, c in enumerate(r):
            if c != '.':
                if c not in antennas:
                    antennas[c] = [(i, j)]
                else:
                    antennas[c].extend([(i, j)])
    return antennas

def find_antinodes(antennas, forever=False):
    antinodes = set()
    for a in antennas:
        anodes = find_antinodes_by_freq(a, antennas[a])
        antinodes = antinodes.union(anodes)
    # print(antinodes)

    return antinodes

def part1():
    antennas = find_antennas()
    antinodes = find_antinodes(antennas)
    # for i, r in enumerate(input):
    #     for j, c in enumerate(r):
    #         print(input[i][j] if (i, j) not in antinodes else '#', end='')
    #     print()
    return len(antinodes)

def part2():
    antennas = find_antennas()
    antinodes = find_antinodes(antennas, True)
    # for i, r in enumerate(input):
    #     for j, c in enumerate(r):
    #         print(input[i][j] if (i, j) not in antinodes else '#', end='')
    #     print()
    return len(antinodes)

example = False
input = read_input(8, example, False)

# execute(part1, "Day 8 - Part 1" + (" - Example" if example else ""))
# Result: 390
# Operation took 3.412700 ms.
execute(part2, "Day 8 - Part 2" + (" - Example" if example else ""))
# Output: 0 - 0.00 ms


