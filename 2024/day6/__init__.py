from typing import Tuple
import time

def turn_right(dx: int, dy: int) -> Tuple[int, int]:
    match (dx, dy):
        case (-1, 0):
            return (0, -1)
        case (1, 0):
            return (0, 1)
        case (0, -1):
            return (1, 0)
        case (0, 1):
            return (-1, 0)
    raise Exception("Unreachable")

def part1(array: list[list[str]], start: Tuple[int, int], direction: Tuple[int, int]) -> int:
    total = 0
    x = start[0]
    y = start[1]
    dx = direction[0]
    dy = direction[1]
    while x >= 0 and x < len(array[0]) and y >= 0 and y < len(array):
        if array[y][x] != "X":
            total += 1
        array[y][x] = "X"
        if y+dy >= 0 and y+dy < len(array) and x+dx >= 0 and x+dx < len(array) and array[y+dy][x+dx] == "#":
            dx, dy = turn_right(dx, dy)
        x += dx
        y += dy
    return total


def loops(array: list[list[str]], start: Tuple[int, int], direction: Tuple[int, int]) -> Tuple[bool, set[Tuple[int, int, int, int]]]:
    past_moves = set()
    x, y = start
    dx, dy = direction
    while x >= 0 and x < len(array[0]) and y >= 0 and y < len(array):
        if y+dy >= 0 and y+dy < len(array) and x+dx >= 0 and x+dx < len(array) and array[y+dy][x+dx] == "#":
            dx, dy = turn_right(dx, dy)
        if (x, y, dx, dy) in past_moves:
            return True, None
        past_moves.add((x, y, dx, dy))
        x += dx
        y += dy
    return False, past_moves

def part2(array: list[list[str]], start: Tuple[int, int], direction: Tuple[int, int]) -> int:
    total = 0
    _, path = loops(array, start, direction)
    print("Normal path calculated")
    space = set((e[0]+e[2],e[1]+e[3]) for e in path if e[0]+e[2] >= 0 and e[0]+e[2] < len(array[0]) and e[1]+e[3] >= 0 and e[1]+e[3] < len(array))
    print(f"{len(space)} positions to test")
    for idx, option in enumerate(space):
        print(f"{idx+1}/{len(space)}", end="\r")
        old = array[option[1]][option[0]]
        array[option[1]][option[0]] = "#"
        does_loop, _ = loops(array, start, direction)
        array[option[1]][option[0]] = old
        if does_loop:
            total += 1
    print()
    return total

def run(part: int, input_data: list[str]):
    array = [list(e) for e in input_data if len(e)]

    start = (0, 0)
    direction = (0, 0)
    for y in range(len(array)):
        for x in range(len(array[0])):
            if array[y][x] in ("", ">", "<", "^", "v"):
                start = (x, y)
                if array[y][x] == ">":
                    direction = (1, 0)
                elif array[y][x] == "<":
                    direction = (-1, 0)
                elif array[y][x] == "^":
                    direction = (0, -1)
                elif array[y][x] == "v":
                    direction = (0, 1)
                break

    print(part1(array, start, direction) if part == 1 else part2(array, start, direction))
