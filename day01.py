import re
from utils import read_file, split_lines

DIGITS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def part1(lines):
    total = 0
    for line in lines:
        digits = re.findall(r"\d", line)
        first_digit = digits[0]
        second_digit = digits[-1]
        total += int(first_digit + second_digit)
    return total


def find_first_digit(line) -> str:
    if line[0].isdigit():
        return line[0]

    # See if string matches any of the keys in DIGITS
    res = next(filter(line.startswith, DIGITS.keys()), None)

    return DIGITS.get(res, None)


def part2(lines):
    total = 0
    for line in lines:
        first_digit = None
        second_digit = None
        for i in range(len(line)):
            first_digit = find_first_digit(line[i:])
            if first_digit:
                break
        for i in range(len(line)):
            second_digit = find_first_digit(line[-1 * i - 1 :])
            if second_digit:
                break
        total += int(first_digit + second_digit)
    return total


input = read_file("inputs/day01.txt")
lines = split_lines(input)


## Part 1
print("--- Part 1 ---")
result1 = part1(lines)
print(result1)

## Part 2
print("--- Part 2 ---")
result2 = part2(lines)
print(result2)
