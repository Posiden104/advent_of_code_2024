from Helpers import *
from collections import defaultdict

def part1():
    space = input.index('\n')
    updates = [[int(page) for page in update.replace('\n', '').split(',')] for update in input[space+1:]]
    rules_dict = defaultdict(list)
    solution = 0

    # each entry in rules_dict is a list of pages that must be after it
    [rules_dict[int(before)].append(int(after)) for rule in [r.replace('\n', '') for r in input[:space]] for before, after in [rule.split("|")]]

    # i = 0
    for update in updates:
        # i += 1
        seen = set()
        update_valid = True
        for page in update:
            page = int(page)
            if len(rules_dict[page]) > 0 and any(pg in seen for pg in rules_dict[page]):
                # print(f"Update {update} is not valid because it breaks rule {page}|{rules_dict[page]}")
                update_valid = False
                break
            seen.add(page)
        if update_valid:
            # valid_rows.append(update)
            # print(f"Update {i} is valid")
            solution += int(update[len(update) // 2])
    return solution

example = False
input: list[str] = read_input(5, example, False)

time_it(part1, "Day 5 - Part 1" + (" - Example" if example else ""))