from utils import read_file
import re


def get_ASCII_code(char, current_value=0):
    value = current_value
    value += ord(char)
    value *= 17
    return value % 256


def hash(string):
    current_value = 0
    for char in string:
        current_value = get_ASCII_code(char, current_value)
    return current_value


if __name__ == "__main__":
    file_input = read_file("inputs/day15.txt")
    strings = file_input.split(",")

    answer_1 = 0
    answer_2 = 0

    print(f"Part 1")
    for string in strings:
        answer_1 += hash(string)

    print(f"{answer_1}")
    print(f"Part 2")
