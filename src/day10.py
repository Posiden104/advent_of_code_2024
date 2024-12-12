from Helpers import *

def walk_trail(r, c, num, seen_trail_ends:set=set(), save_ends=True) -> int:
    score = 0
    if r < 0 or r >= len(input) or c < 0 or c >= len(input[r]):
        return 0
    if ((r,c) not in seen_trail_ends) and (int(input[r][c]) == 9 or num == 9):
        if save_ends: seen_trail_ends.add((r, c))
        return 1
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i != 0 and j != 0) or (r+i < 0 or r+i >= len(input) or c+j < 0 or c+j >= len(input[r])) or i == 0 and j == 0:
                continue
            if input[r+i][c+j] != '.' and int(input[r+i][c+j]) == (num + 1):
                res = walk_trail(r+i, c+j, int(input[r+i][c+j]), seen_trail_ends, save_ends)
                if res > 0:
                    if save_ends: seen_trail_ends.add((r+i, c+j))
                    score += res
    return score
    
def part1(save_ends=True):
    score = 0
    for r in range(len(input)):
        for c in range(len(input[r])):
            if input[r][c] == '0':
                sc = walk_trail(r, c, 0, set(), save_ends)
                score += sc
    return score

def part2():
    # just the same as part 1, but dont save trail ends
    return part1(False)

# example = True
example = False
input = read_input(10, example, False)

execute(part1, "Day 10 - Part 1" + (" - Example" if example else ""))
# Output: 682 - 72.14 ms
execute(part2, "Day 10 - Part 2" + (" - Example" if example else ""))
# Output: 1511 - 62.59 ms