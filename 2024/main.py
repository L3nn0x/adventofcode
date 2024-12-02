import argparse
import importlib
import sys

def main(day: int, input_data: list[str]):
    day = "day" + str(day)
    module = importlib.import_module(day)
    module.run(input_data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code 2024")
    parser.add_argument("day", type=int, help="The day to run.")
    parser.add_argument("-f", "--file", type=str, help="The input data file.")

    args = parser.parse_args()

    if not sys.stdin.isatty():
        raw_data = sys.stdin.read()
    elif args.file:
        try:
            with open(args.file, "r") as fp:
                raw_data = fp.read()
        except FileNotFoundError:
            print(f"File {args.file} not found")
            exit(1)
    else:
        print("No input data provided, either pipe some data or provice a filename")
        exit(1)
    data = [line.strip() for line in raw_data.splitlines() if line.strip()]
    main(args.day, data)
