from Helpers import *
from collections import defaultdict

bad_updates = []
rules_dict = defaultdict(list)

def part1():
    space = input.index('\n')
    updates = [[int(page) for page in update.replace('\n', '').split(',')] for update in input[space+1:]]
    solution = 0

    # each entry in rules_dict is a list of pages that must be after it
    [rules_dict[int(before)].append(int(after)) for rule in [r.replace('\n', '') for r in input[:space]] for before, after in [rule.split("|")]]

    for update in updates:
        seen = set()
        update_valid = True
        for page in update:
            if len(rules_dict[page]) > 0 and any(pg in seen for pg in rules_dict[page]):
                bad_updates.append(update)
                update_valid = False
                break
            seen.add(page)
        if update_valid:
            solution += int(update[len(update) // 2])
    return solution

def find_next_number(relevant_rules):
    for r in relevant_rules:
        if not any(r in rule for rule in relevant_rules.values()):
            return r

def fix_update(update):
    # for index_of_page, page in enumerate(update):
    #     indices_of_later_pages = [i for i, x in enumerate(update) if x in rules_dict[page]]
    #     for index in indices_of_later_pages:
    #         if index_of_page > index:
    #             print(f"Update {update} is not valid because it breaks rule {page}|{update[index]}")
    
    # print(f"Fixing update {update}")
    relevant_rules = {page: set(rules_dict[page]) for page in update}
    new_update = []
    while len(new_update) < len(update):
        next = find_next_number(relevant_rules)
        new_update.append(next)
        relevant_rules.pop(next)
    return new_update

def part2():
    part1()
    solution = 0
    for bad in bad_updates:
        fixed = fix_update(bad)
        solution += int(fixed[len(fixed) // 2])
    return solution


example = False
input: list[str] = read_input(5, example, False)

# execute(part1, "Day 5 - Part 1" + (" - Example" if example else ""))
execute(part2, "Day 5 - Part 2" + (" - Example" if example else ""))