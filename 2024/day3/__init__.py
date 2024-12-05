from typing import Optional

# takes a string and returns the parsed number and the next element to be parsed
def parse_number(data: str) -> (Optional[int], int):
    number = None
    index = 0
    while index != len(data) and data[index].isdigit():
        index += 1
    if not data[:index].isdigit() or index > 3:
        return (None, min(index, 3))
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
    return ((n1, n2), index+1)

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
        index += max(idx, 1)
        if res:
            total += res
    return total

def part2(enabled: bool, line: str) -> int:
    total = 0
    index = 0
    while index < len(line):
        res, idx = parse_mul(line[index:])
        to_enable, idx2 = parse_conditional(line[index:])
        index += max(max(idx, idx2), 1)
        if to_enable is not None:
            enabled = to_enable
        if enabled and res:
            total += res[0] * res[1]
    return enabled, total

def run(part: int, input_data: list[str]):
    enabled = True
    total = 0
    for line in input_data:
        if part == 1:
            total += part1(line)
        else:
            enabled, tmp = part2(enabled, line)
            total += tmp
    print(total)

def test():
    assert parse_number("") == (None, 0)
    assert parse_number("a") == (None, 0)
    assert parse_number("1") == (1, 1)
    assert parse_number("123") == (123, 3)
    assert parse_number("1234") == (None, 3)
    assert parse_number("1,") == (1, 1)

    assert parse_mul("") == (None, 0)
    assert parse_mul("a") == (None, 0)
    assert parse_mul("mul (1,2)") == (None, 0)
    assert parse_mul("mul(a,1)") == (None, 4)
    assert parse_mul("mul(1, 1)") == (None, 6)
    assert parse_mul("mul(16,a)") == (None, 7)
    assert parse_mul("mul(16,1!") == (None, 8)
    assert parse_mul("mul(1,2)") == (2, 8)
    assert parse_mul("mul(123,234)") == (123*234, 12)

    assert parse_conditional("") == (None, 0)
    assert parse_conditional("a") == (None, 0)
    assert parse_conditional("do()") == (True, 4)
    assert parse_conditional("don't()") == (False, 7)
    assert parse_conditional("do't()") == (None, 0)

    assert part2("abcmulmul(1,2)m[2,4/]don't()do()don't()mul(2,3)do()mul(3,3)") == 1*2+3*3

if __name__ == "__main__":
    test()
