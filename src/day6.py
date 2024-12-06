from Helpers import *
from concurrent.futures import ThreadPoolExecutor, as_completed
from copy import deepcopy

'''
    0
  3   1
    2
'''
routes = {'|', '-', '+', 'X'}
obstacles = {'#', 'O'}

def up(pos, map):
    new_x = 0
    for i in range(pos[0], -1, -1):
        if map[i][pos[1]] in obstacles:
            return False, (i + 1, pos[1]), new_x
        elif map[i][pos[1]] not in routes:
            map[i][pos[1]] = '|'
            new_x += 1
        elif map[i][pos[1]] == '-':
            map[i][pos[1]] = '+'
    return True, None, new_x
def right(pos, map):
    new_x = 0
    for i in range(pos[1], len(map[pos[0]])):
        if map[pos[0]][i] in obstacles:
            return False, (pos[0], i - 1), new_x
        elif map[pos[0]][i] not in routes:
            map[pos[0]][i] = '-'
            new_x += 1
        elif map[pos[0]][i] == '|':
            map[pos[0]][i] = '+'
    return True, None, new_x
def down(pos, map):
    new_x = 0
    for i in range(pos[0], len(map)):
        if map[i][pos[1]] in obstacles:
            return False, (i - 1, pos[1]), new_x
        elif map[i][pos[1]] not in routes:
            map[i][pos[1]] = '|'
            new_x += 1
        elif map[i][pos[1]] == '-':
            map[i][pos[1]] = '+'
    return True, None, new_x
def left(pos, map):
    new_x = 0
    for i in range(pos[1], -1, -1):
        if map[pos[0]][i] in obstacles:
            return False, (pos[0], i + 1), new_x
        elif map[pos[0]][i] not in routes:
            map[pos[0]][i] = '-'
            new_x += 1
        elif map[pos[0]][i] == '|':
            map[pos[0]][i] = '+'
    return True, None, new_x

def print_map(map = None):
    print('\n\n\n')
    for r in map or input:
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

def walk_maze(start_pos = None, provided_input = None):
    walk = [up, right, down, left]
    dir = 0
    pos = start_pos or find_pos()
    pos_visited = 0
    loop_found = False
    route_repeat = 0
    exited = False
    if not provided_input:
        map = deepcopy(input)
    else:
        map = provided_input
    while(not exited):
        exited, pos, visited = walk[dir](pos, map)
        pos_visited += visited
        if visited == 0:
            route_repeat += 1
            if route_repeat > 3:
                loop_found = True
                break
        dir = (dir + 1) % 4
        if(not exited):
            map[pos[0]][pos[1]] = '+'
    return pos_visited, loop_found

def process_new_obstacle(r, c, start_pos):
    loops = 0
    map = deepcopy(input)
    if map[r][c] == '.':
        map[r][c] = 'O'
        _, looped = walk_maze(start_pos, map)
        if looped:
            loops += 1
        map[r][c] = '.'
    return loops

def part1():
    distinct_count = walk_maze()[0]
    # print_map()
    return distinct_count

def part2():
    start_pos = find_pos()
    loops = 0
    tasks = []
    with ThreadPoolExecutor() as executor:
        for r in range(len(input)):
            print(f"placing blocks on row {r} of {len(input)}\n")
            for c in range(len(input[r])):
                tasks.append(executor.submit(process_new_obstacle, r, c, start_pos))
        for future in as_completed(tasks):
            loops += future.result()
    return loops
                

example = False
input = read_input(6, example, False)

# execute(part1, "Day 6 - Part 1" + (" - Example" if example else ""))
execute(part2, "Day 6 - Part 2" + (" - Example" if example else ""))
# Output: 2264 Too High 8.6 mins
# Output: 2262 correct 9.314824 mins