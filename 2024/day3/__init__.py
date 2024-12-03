from typing import Optional

# takes a string and returns the parsed number and the next element to be parsed
def parse_number(data: str) -> (Optional[int], int):
    number = None
    index = 0
    while index != len(data) and data[index].isdigit():
        index += 1
    if not data[:index].isdigit() or index > 3:
        return (None, index)
    return (int(data[:index]), index)

# returns result + next element to be parsed
def parse_mul(data: str) -> (Optional[int], int):
    if data[:4] != "mul(":
        return (None, 0)
    n1, index = parse_number(data[4:])
    index += 4
    if n1 is None:
        return (None, index)
    if data[index] != ",":
        return (None, index)
    n2, idx = parse_number(data[index+1:])
    index += 1 + idx
    if n2 is None:
        return (None, index)
    if data[index] != ")":
        return (None, index)
    return (n1 * n2, index+1)

def parse_conditional(data: str) -> (Optional[bool], int):
    if data[:4] == "do()":
        return (True, 4)
    if data[:7] == "don't()":
        return (False, 7)
    return (None, 0)

def part1(line: str) -> int:
    total = 0
    index = 0
    while index <= len(line):
        res, idx = parse_mul(line[index:])
        index += idx
        if res:
            total += res
    return total

def part2(line: str) -> int:
    total = 0
    index = 0
    enabled = True
    while index <= len(line):
        res, idx = parse_mul(line[index:])
        print(f"{'disabled' if not enabled else 'enabled'} mul check {index} {idx} '{line[index:]}'")
        index += idx
        to_enable, idx = parse_conditional(line[index:])
        print(f"{'disabled' if not enabled else 'enabled'} do  check {index} {idx} '{line[index:]}'")
        index += idx if idx else 1
        if to_enable is not None:
            enabled = to_enable
        if enabled and res:
            total += res
    return total

def run(part: int, input_data: list[str]):
    print(sum(map(lambda e: part1(e) if part == 1 else part2(e), input_data[:1])))
