from Helpers import *

def expand_map():
    blocks = []
    is_free = False
    blockId = 0
    for num in input:
        if not is_free:
            blocks.extend([str(blockId)] * int(num))
            blockId += 1
        else:
            blocks.extend(['.'] * int(num))
        is_free = not is_free
    return blocks
    

def print_blocks(blocks):
    print(str.join('', blocks))

def part1():
    blocks = expand_map()
    dots = set(i for i, c in enumerate(blocks) if c == '.')

    min_idx = min(dots)

    for i in range(len(blocks) - 1, 0, -1):
        if min_idx > i:
            break
        if i not in dots:
            min_idx = min(dots)
            blocks[i], blocks[min_idx] = blocks[min_idx], blocks[i]
            dots.remove(min_idx)
            dots.add(i)
        min_idx = min(dots)
        
    blocks = blocks[:min_idx]
    checksum = sum(i * int(c) for i, c in enumerate(blocks))
    return checksum

def part2():
    pass


example = False
input = read_input(9, example, True)

execute(part1, "Day 9 - Part 1" + (" - Example" if example else ""))
# Output: 6448989155953 - 38.84 ms
# execute(part2, "Day 9 - Part 2" + (" - Example" if example else ""))