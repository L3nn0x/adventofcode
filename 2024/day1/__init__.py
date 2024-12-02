def part1(l1: list[int], l2: list[int]) -> int:
    return sum(abs(a - b) for a, b in zip(l1, l2))

def part2(l1: list[int], l2: list[int]) -> int:
    score = 0
    for e in l1:
        score += e * l2.count(e)
    return score


def run(part: int, input_data: list[str]):
    l1 = []
    l2 = []
    for line in input_data:
        data = [e for e in line.split(" ") if e]
        l1.append(int(data[0].strip()))
        l2.append(int(data[1].strip()))
    l1.sort()
    l2.sort()
    print(part1(l1, l2) if part == 1 else part2(l1, l2))
