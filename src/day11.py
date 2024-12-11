from Helpers import *
from concurrent.futures import ThreadPoolExecutor, as_completed

def blink(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        s = str(stone)
        return [int(s[:len(s)//2]), int(s[len(s)//2:])]
    else:
        return [stone * 2024]

def stone_blink(stones):
    new_state = []
    for stone in stones:
        if stone == 0:
            new_state.append(1)
        elif len(str(stone)) % 2 == 0:
            s = str(stone)
            new_state.append(int(s[:len(s)//2]))
            new_state.append(int(s[len(s)//2:]))
        else:
            new_state.append(stone * 2024)
    return new_state


def count_levels(stone, level, target):
    count = 0
    if level == target:
        level_memos[level][stone] = 1
        return 1
    if stone in level_memos[level]:
        return level_memos[level][stone]
    nxt_level = blink(stone)
    for nxt_stone in nxt_level:
        ct = count_levels(nxt_stone, level + 1, target)
        count += ct
    level_memos[level][stone] = count
    return count
            

def part1():
    stones = [int(x) for x in input.split(' ')]
    
    for i in range(25):
        stones = stone_blink(stones)
        # print(stones)
    return len(stones)

depth = 75
level_memos = [{} for _ in range(depth + 1)]

def part2():
    stones = [int(x) for x in input.split(' ')]
    count = 0
    for stone in stones:
        count += count_levels(stone, 0, depth)

    return count

example = False
input = read_input(11, example, True)

# execute(part1, "Day 11 - Part 1" + (" - Example" if example else ""))
# Output: 198089 - 513.981800 ms
execute(part2, "Day 11 - Part 2" + (" - Example" if example else ""))
# Result: 236302670835517
# Operation took 382.750400 ms.

