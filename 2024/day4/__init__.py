def explore_letter_inner(array: list[str], x: int, y: int, direction: (int, int)) -> bool:
    word = ""
    dx, dy = direction
    for i in range(4):
        word += array[y][x]
        x += dx
        y += dy
        if x < 0 or x >= len(array[0]) or y < 0 or y >= len(array):
            break
    return word == "XMAS"

def explore_letter(array: list[str], x: int, y: int) -> int:
    w = 0
    if array[y][x] == "X" or array[y][x] == "S":
        w = int(explore_letter_inner(array, x, y, (-1, -1))) # top left
        w += int(explore_letter_inner(array, x, y, (-1, 0))) # left
        w += int(explore_letter_inner(array, x, y, (-1, 1))) # down left
        w += int(explore_letter_inner(array, x, y, (0, 1))) # down
        w += int(explore_letter_inner(array, x, y, (1, 1))) # down right
        w += int(explore_letter_inner(array, x, y, (1, 0))) # right
        w += int(explore_letter_inner(array, x, y, (1, -1))) # up right
        w += int(explore_letter_inner(array, x, y, (0, -1))) # up
    return w

def part1(input_data: list[str]) -> int:
    total = 0
    for y in range(len(input_data)):
        for x in range(len(input_data[0])):
            total += explore_letter(input_data, x, y)
    return total

def explore_xmas(array: list[str], x: int, y: int) -> int:
    if array[y][x] == "A":
        if x - 1 >= 0 and y - 1 >= 0 and x + 1 < len(array[0]) and y + 1 < len(array):
            diag1 = array[y-1][x-1] + array[y][x] + array[y+1][x+1]
            diag2 = array[y-1][x+1] + array[y][x] + array[y+1][x-1]
            if (diag1 == "MAS" or diag1 == "SAM") and (diag2 == "MAS" or diag2 == "SAM"):
                return 1
    return 0

def part2(input_data: list[str]) -> int:
    total = 0
    for y in range(len(input_data)):
        for x in range(len(input_data[0])):
            total += explore_xmas(input_data, x, y)
    return total

def run(part: int, input_data: list[str]):
    print(part1(input_data) if part == 1 else part2(input_data))
