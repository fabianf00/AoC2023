from utils import read_file, split_lines
import re


def transpose(pattern):
    transposed_pattern = ["" for _ in range(len(pattern[0]))]

    for line in pattern:
        for i, char in enumerate(line):
            transposed_pattern[i] += char

    return transposed_pattern


def is_reflection(pattern, reflection_index):
    distance = min(reflection_index, len(pattern) - reflection_index)

    for i in range(distance):
        if pattern[reflection_index - i - 1] != pattern[reflection_index + i]:
            return False

    return True


def get_reflection_index(pattern):
    for reflection_index in range(1, len(pattern) - 1):
        if is_reflection(pattern, reflection_index):
            return reflection_index

    return 0


def get_pattern_note(pattern):
    reflection_index = 0

    reflection_index = 100 * get_reflection_index(pattern)

    if not reflection_index:
        transposed_pattern = transpose(pattern)
        return get_reflection_index(transposed_pattern)

    return reflection_index


if __name__ == "__main__":
    file_input = read_file("inputs/day13.txt")
    patterns = list(map(split_lines, file_input.split("\n\n")))

    answer_1 = 0
    answer_2 = 0

    print("Part 1")

    for pattern in patterns:
        answer_1 += get_pattern_note(pattern)

    print(answer_1)

    print("Part 2")

    print(answer_2)
