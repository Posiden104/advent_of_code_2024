from Helpers import *

'''
00 X 10 M 20 A 30 S
01 M 11 M
02 A      22 A
03 S           33 S

'''

def xmas_count(x_loc, puzzle):
    count = 0
    y = x_loc[0]
    x = x_loc[1]
        

    try:
        if puzzle[y + 1][x] == 'M' and puzzle[y + 2][x] == 'A' and puzzle[y + 3][x] == 'S':
            count += 1
    except IndexError:
        pass
    try:
        if puzzle[y][x + 1] == 'M' and puzzle[y][x + 2] == 'A' and puzzle[y][x + 3] == 'S':
            count += 1
    except IndexError:
        pass
    try:
        if puzzle[y + 1][x + 1] == 'M' and puzzle[y + 2][x + 2] == 'A' and puzzle[y + 3][x + 3] == 'S':
            count += 1
    except IndexError:
        pass
    if y - 3 >= 0:
        try:
            if puzzle[y - 1][x] == 'M' and puzzle[y - 2][x] == 'A' and puzzle[y - 3][x] == 'S':
                count += 1
        except IndexError:
            pass
        try:
            if puzzle[y - 1][x + 1] == 'M' and puzzle[y - 2][x + 2] == 'A' and puzzle[y - 3][x + 3] == 'S':
                count += 1
        except IndexError:
            pass
    if x - 3 >= 0:
        try:
            if puzzle[y][x - 1] == 'M' and puzzle[y][x - 2] == 'A' and puzzle[y][x - 3] == 'S':
                count += 1
        except IndexError:
            pass
        try:
            if puzzle[y + 1][x - 1] == 'M' and puzzle[y + 2][x - 2] == 'A' and puzzle[y + 3][x - 3] == 'S':
                count += 1
        except IndexError:
            pass
    if y - 3 >= 0 and x - 3 >= 0:
        try:
            if puzzle[y - 1][x - 1] == 'M' and puzzle[y - 2][x - 2] == 'A' and puzzle[y - 3][x - 3] == 'S':
                count += 1
        except IndexError:
            pass
    
    return count

def mas_count(a_loc, puzzle):

    count = 0
    y = a_loc[0]
    x = a_loc[1]

    if y - 1 < 0 or x - 1 < 0 or y + 1 >= len(puzzle) or x + 1 >= len(puzzle[y]):
        return 0

    try:
        tl = puzzle[y - 1][x - 1]
        tr = puzzle[y - 1][x + 1]
        bl = puzzle[y + 1][x - 1]
        br = puzzle[y + 1][x + 1]
        
        if not (tl == 'X' or tr == 'X' or bl == 'X' or br == 'X' or tl == 'A' or tr == 'A' or bl == 'A' or br == 'A') and ((tl == tr and (tl == 'M' or tl == 'S') and bl == br and tl != bl) or (tl == bl and (tl == 'M' or tl == 'S') and tr == br and tl != tr)):
            count += 1
        
        # print("=========================================")
        # print(f"{tl}.{tr}\n.{puzzle[y][x]}.\n{bl}.{br}")
        # print('----')        
        # print(count)

    except IndexError:
        pass
    

    return count
    
def part1():
    puzzle = [line.replace('\n', '') for line in input]
    solution = 0
    
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == 'X':
                solution += xmas_count((i, j), puzzle)
    return solution

def part2():
    puzzle = [line.replace('\n', '') for line in input]
    solution = 0

    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == 'A':
                solution += mas_count((i, j), puzzle)
    return solution
    # Output: 2047 too high
    # Output: 1965 ✅

input = read_input(4, False, False)

time_it(part2)