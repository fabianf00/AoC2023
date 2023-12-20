from utils import read_file, split_lines
import re
from functools import lru_cache


@lru_cache(maxsize=None)
def get_combinations(records, groups, current_length=0):
    if not records:
        if (
            not groups
            and current_length == 0
            or len(groups) == 1
            and groups[0] == current_length
        ):
            return 1
        else:
            return 0

    if groups and current_length > groups[0] or not groups and current_length != 0:
        return 0

    character, records = records[0], records[1:]
    total_combinations = 0

    # ? is treated as #
    if character in "#?":
        total_combinations += get_combinations(records, groups, current_length + 1)

    # . is treated as .
    if character in ".?":
        if current_length == 0:
            total_combinations += get_combinations(records, groups)
        elif current_length == groups[0]:
            total_combinations += get_combinations(records, groups[1:])

    return total_combinations


if __name__ == "__main__":
    file_input = read_file("inputs/day12.txt")
    lines = split_lines(file_input)

    answer_1 = 0
    answer_2 = 0

    print("Part 1")
    for line in lines:
        records, groups = line.split()
        groups = tuple(map(int, re.findall(r"\d+", groups)))
        answer_1 += get_combinations(records, groups)

    print(answer_1)

    print("Part 2")
    for line in lines:
        records, groups = line.split()
        records = "?".join([records] * 5)
        groups = ",".join([groups] * 5)
        groups = tuple(map(int, re.findall(r"\d+", groups)))
        answer_2 += get_combinations(records, groups)

    print(answer_2)
