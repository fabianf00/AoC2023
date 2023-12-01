import re

DIGITS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def read_file(file_name) -> str:
    with open(file_name) as f:
        return f.read().rstrip()


def split_lines(input) -> list:
    return input.split("\n")


def check_digit(char) -> int:
    if char.isdigit():
        return int(char)


def part1(lines):
    calibration_values = []
    for line in lines:
        digits = re.findall(r"\d", line)
        first_digit = digits[0]
        second_digit = digits[-1]
        calibration_values.append(int(first_digit + second_digit))
    return sum(calibration_values)


## Part 1
input = read_file("part_1.txt")
lines = split_lines(input)

result = part1(lines)

print(result)

## Part 2
