from collections import defaultdict

def part1(rules: defaultdict(set), updates: list[list[int]]) -> int:
    total = 0
    for update in updates:
        good = True
        for idx, first_page in enumerate(update):
            for second_page in update[idx+1:]:
                if second_page in rules and first_page in rules[second_page]:
                    good = False
                    break
            if not good:
                break
        if good:
            total += update[int(len(update)/2)]
    return total

def part2(rules: defaultdict(set), updates: list[list[int]]) -> int:
    total = 0
    for update in updates:
        good = True
        for idx, first_page in enumerate(update):
            for idx2, second_page in enumerate(update[idx+1:]):
                if second_page in rules and first_page in rules[second_page]:
                    good = False
                    update[idx] = second_page
                    update[idx2+idx+1] = first_page
                    first_page = second_page
        if not good:
            total += update[int(len(update)/2)]
    return total

def run(part: int, input_data: list[str]):
    rules = defaultdict(set)
    for idx, r in enumerate(input_data):
        if not len(r):
            break
        rule = r.split("|")
        rules[int(rule[0])].add(int(rule[1]))

    updates = []
    for update in input_data[idx+1:]:
        if update == "":
            continue
        update = update.split(",")
        if not len(update):
            continue
        updates.append(list(map(lambda e: int(e), update)))

    print(part1(rules, updates) if part == 1 else part2(rules, updates))
