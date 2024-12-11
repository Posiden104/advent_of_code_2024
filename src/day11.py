from Helpers import *

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

def part1():
    stones = [int(x) for x in input.split(' ')]
    
    for i in range(25):
        stones = stone_blink(stones)
        # print(stones)
    return len(stones)

def part2():
    pass

example = False
input = read_input(11, example, True)

execute(part1, "Day 11 - Part 1" + (" - Example" if example else ""))
# Output: 0 - 0.00 ms
execute(part2, "Day 11 - Part 2" + (" - Example" if example else ""))
# Output: 0 - 0.00 ms
