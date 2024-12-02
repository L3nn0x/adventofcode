def run(input_data: list[str]):
    l1 = []
    l2 = []
    for line in input_data:
        data = [e for e in line.split(" ") if e]
        l1.append(int(data[0].strip()))
        l2.append(int(data[1].strip()))
    l1.sort()
    l2.sort()
    print(sum(abs(a - b) for a, b in zip(l1, l2)))
