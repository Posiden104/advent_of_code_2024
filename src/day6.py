from Helpers import *

'''
    0
  3   1
    2
'''

def up(pos):
    new_x = 0
    for i in range(pos[0], -1, -1):
        if input[i][pos[1]] == '#':
            return False, (i + 1, pos[1]), new_x
        elif not input[i][pos[1]] == 'X':
            input[i][pos[1]] = 'X'
            new_x += 1
    return True, None, new_x
def right(pos):
    new_x = 0
    for i in range(pos[1], len(input[pos[0]])):
        if input[pos[0]][i] == '#':
            return False, (pos[0], i - 1), new_x
        elif not input[pos[0]][i] == 'X':
            input[pos[0]][i] = 'X'
            new_x += 1
    return True, None, new_x
def down(pos):
    new_x = 0
    for i in range(pos[0], len(input)):
        if input[i][pos[1]] == '#':
            return False, (i - 1, pos[1]), new_x
        elif not input[i][pos[1]] == 'X':
            input[i][pos[1]] = 'X'
            new_x += 1
    return True, None, new_x
def left(pos):
    new_x = 0
    for i in range(pos[1], -1, -1):
        if input[pos[0]][i] == '#':
            return False, (pos[0], i + 1), new_x
        elif not input[pos[0]][i] == 'X':
            input[pos[0]][i] = 'X'
            new_x += 1
    return True, None, new_x

def print_map():
    for r in input:
        print(''.join(r))

def find_pos():
    pos = None
    for i, r in enumerate(input):
        input[i] = list(r)
        if not pos:
            for j, c in enumerate(input[i]):
                if c == '^':
                    pos = (i, j)
    return pos

def walk_maze():
    walk = [up, right, down, left]
    dir = 0
    pos = find_pos()
    pos_visited = 0
    exited = False
    while(not exited):
        exited, pos, visited = walk[dir](pos)
        pos_visited += visited
        dir = (dir + 1) % 4
        # print_map()
    return pos_visited

def part1():
    return walk_maze()

def part2():
    pass

example = False
input = read_input(6, example, False)

execute(part1, "Day 6 - Part 1" + (" - Example" if example else ""))
execute(part2, "Day 6 - Part 2" + (" - Example" if example else ""))