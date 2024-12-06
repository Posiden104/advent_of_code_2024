from Helpers import *
from concurrent.futures import ThreadPoolExecutor, as_completed
from copy import deepcopy

'''
    0
  3   1
    2
'''
routes = {'|', '-', '+'}
obstacles = {'#', 'O'}

def up_x(pos, map):
    for i in range(pos[0], -1, -1):
        if map[i][pos[1]] == '#':
            return False, (i + 1, pos[1])
        elif not map[i][pos[1]] == 'X':
            map[i][pos[1]] = 'X'
    return True, None

def right_x(pos, map):
    for i in range(pos[1], len(map[pos[0]])):
        if map[pos[0]][i] == '#':
            return False, (pos[0], i - 1)
        elif not map[pos[0]][i] == 'X':
            map[pos[0]][i] = 'X'
    return True, None

def down_x(pos, map):
    for i in range(pos[0], len(map)):
        if map[i][pos[1]] == '#':
            return False, (i - 1, pos[1])
        elif not map[i][pos[1]] == 'X':
            map[i][pos[1]] = 'X'
    return True, None

def left_x(pos, map):
    for i in range(pos[1], -1, -1):
        if map[pos[0]][i] == '#':
            return False, (pos[0], i + 1)
        elif not map[pos[0]][i] == 'X':
            map[pos[0]][i] = 'X'
    return True, None

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

def fill_map(start_pos = None):
    walk = [up_x, right_x, down_x, left_x]
    dir = 0
    pos = start_pos
    exited = False
    map = input

    while(not exited):
        exited, pos = walk[dir](pos, map)
        dir = (dir + 1) % 4
    return map 

def walk_maze(start_pos = None, provided_input = None):
    global walks
    walks += 1
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
    return pos_visited, loop_found, map


def process_new_obstacle(r, c, start_pos, provided_map):
    loops = 0
    map = deepcopy(provided_map)
    # # - 16064 walks 9.6 min
    # X - 5534 walks 10.35 min
    if map[r][c] == 'X':
        save = map[r][c]
        map[r][c] = 'O'
        _, looped, _ = walk_maze(start_pos, map)
        if looped:
            loops += 1
        map[r][c] = save
    return loops

def part1():
    distinct_count = walk_maze()[0]
    # print_map()
    return distinct_count

def part2():
    start_pos = find_pos()
    # count_dot = sum(row.count('.') for row in input)
    # print(f"count .: {count_dot}")
    map = fill_map(start_pos)
    # count = sum(row.count('X') for row in map)
    # count_dot = sum(row.count('.') for row in map)
    # print(f"count X: {count}")
    # print(f"count .: {count_dot}")
    # return 0
    loops = 0
    tasks = []
    with ThreadPoolExecutor() as executor:
        for r in range(len(input)):
            print(f"placing blocks on row {r} of {len(input)}\n")
            for c in range(len(input[r])):
                tasks.append(executor.submit(process_new_obstacle, r, c, start_pos, map))
        for future in as_completed(tasks):
            loops += future.result()
    print(f"Walks: {walks}")
    return loops
                

example = False
input = read_input(6, example, False)
walks = 0

# execute(part1, "Day 6 - Part 1" + (" - Example" if example else ""))
execute(part2, "Day 6 - Part 2" + (" - Example" if example else ""))
# Output: 2264 Too High 8.6 mins
# Output: 2262 correct 9.314824 mins