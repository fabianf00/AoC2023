from utils import read_file, split_lines
from collections import defaultdict

not_symbols = set("0123456789.")
test_input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


def expand_number(start_column, row):
    number = row[start_column]
    length = 1
    while start_column + length < len(row) and row[start_column + length].isdigit():
        number += row[start_column + length]
        length += 1
    return int(number), length


def is_adjacent_to_symbol(lines, row_idx, start_column, length):
    upper_row_index = row_idx - 1 if row_idx > 0 else 0
    lower_row_index = row_idx + 1 if row_idx < len(lines) - 1 else row_idx

    start_column_index = start_column - 1 if start_column > 0 else 0
    end_column_index = (
        start_column + length
        if start_column + length < len(lines[0]) - 1
        else len(lines[0]) - 1
    )

    is_adjacent = False
    gear_positions = []

    for row_index in range(upper_row_index, lower_row_index + 1):
        for col_index in range(start_column_index, end_column_index + 1):
            if lines[row_index][col_index] not in not_symbols:
                is_adjacent = True
                # check if symbol is * (Part2)
                if lines[row_index][col_index] is "*":
                    gear_positions.append((row_index, col_index))

    return is_adjacent, gear_positions


if __name__ == "__main__":
    testing = False
    if testing:
        lines = split_lines(test_input)
    else:
        file_input = read_file("inputs/day03.txt")
        lines = split_lines(file_input)

    answer_1 = 0
    answer_2 = 0

    gear_list = defaultdict(list)

    print("--- Part 1 ---")
    number_rows = len(lines)
    number_cols = len(lines[0])

    for r_idx, row in enumerate(lines):
        col_idx = 0
        while col_idx < number_cols:
            if not row[col_idx].isdigit():
                col_idx += 1
                continue
            number, length = expand_number(col_idx, row)
            is_adjacent, gear_pos = is_adjacent_to_symbol(lines, r_idx, col_idx, length)
            if is_adjacent:
                answer_1 += number
                # Part 2
                for gear in gear_pos:
                    gear_list[gear].append(number)
            col_idx += length

    print(f"Answer 1: {answer_1}")
    print("--- Part 2 ---")
    answer_2 = sum(
        map(
            lambda elements: elements[0] * elements[1],
            filter(lambda x: len(x) == 2, gear_list.values()),
        )
    )
    print(f"Answer 2: {answer_2}")
