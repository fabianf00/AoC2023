from utils import read_file
import re
from collections import defaultdict


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


def split_string(string):
    seperator = " "
    if "-" in string:
        seperator = "-"
    elif "=" in string:
        seperator = "="
    else:
        seperator = " "

    return *string.split(seperator), seperator


def conatains_lense_label(box, lense_lable):
    for index, (label, focal_length) in enumerate(box):
        if label == lense_lable:
            return True, index
    return False, -1


def update_box(box, lense_lable, focal_length, operation):
    is_present, index = conatains_lense_label(box, lense_lable)

    if operation == "-":
        if is_present:
            box.pop(index)
    elif operation == "=":
        if is_present:
            box[index] = (lense_lable, focal_length)
        else:
            box.append((lense_lable, focal_length))
    return box


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

    boxes = defaultdict(list)

    for string in strings:
        lense_lable, focal_length, operation = split_string(string)
        hash_value = hash(lense_lable)

        boxes[hash_value] = update_box(
            boxes[hash_value], lense_lable, focal_length, operation
        )

    for box_number, box in boxes.items():
        for pos, (label, focal_length) in enumerate(box, 1):
            answer_2 += (1 + box_number) * pos * int(focal_length)

    print(f"{answer_2}")
