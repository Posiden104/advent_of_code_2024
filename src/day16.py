from Helpers import *
from functools import cache
from collections import deque
import heapq

# Directions: (dy, dx, direction)
DIRECTIONS = [
    (-1, 0, 'N'),  # North
    (0, 1, 'E'),   # East
    (1, 0, 'S'),   # South
    (0, -1, 'W')   # West
]

def find_start_end(grid):
    start = end = None
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 'S':
                start = (y, x)
            elif cell == 'E':
                end = (y, x)
    return start, end

def bfs(grid, start, end):
    height = len(grid)
    width = len(grid[0])
    start_y, start_x = start
    end_y, end_x = end

    # Priority queue: (cost, y, x, direction)
    pq = [(0, start_y, start_x, 'E')]
    visited = set()

    while pq:
        cost, y, x, direction = heapq.heappop(pq)

        if (y, x) == end:
            return cost

        if (y, x, direction) in visited:
            continue

        visited.add((y, x, direction))

        for dy, dx, new_direction in DIRECTIONS:
            new_y, new_x = y + dy, x + dx
            if 0 <= new_y < height and 0 <= new_x < width and grid[new_y][new_x] != '#':
                if new_direction == direction:
                    new_cost = cost + 1
                else:
                    new_cost = cost + 1001
                heapq.heappush(pq, (new_cost, new_y, new_x, new_direction))

        # # Rotate clockwise and counterclockwise
        # for i in [-1, 1]:
        #     new_direction_index = (DIRECTIONS.index((dy, dx, direction)) + i) % 4
        #     new_direction = DIRECTIONS[new_direction_index][2]
        #     new_cost = cost + 1000
        #     heapq.heappush(pq, (new_cost, y, x, new_direction))

    return float('inf')

def part1():
    start, end = find_start_end(input)
    return bfs(input, start, end)

def part2():
    pass

example = False
input = read_input(16, example, False)
height = len(input)
width = len(input[0])

#example input:
'''
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
'''

execute(part1, "Day 16 - Part 1" + (" - Example" if example else ""))
'''
Result: 85480
Operation took 109.735200 ms.
'''

execute(part2, "Day 16 - Part 2" + (" - Example" if example else ""))
'''
Result: 0
Operation took 0 ms.
'''

