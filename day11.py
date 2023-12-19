from utils import read_file, split_lines
import re


def get_grid_information(grid):
    row_count = [0 for _ in range(len(grid))]
    col_count = [0 for _ in range(len(grid[0]))]

    expanding_rows = []
    expanding_cols = []
    galaxies = []

    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col == "#":
                row_count[r] += 1
                col_count[c] += 1
                galaxies.append((r, c))

    for r in range(len(row_count)):
        if row_count[r] == 0:
            expanding_rows.append(r)

    for c in range(len(col_count)):
        if col_count[c] == 0:
            expanding_cols.append(c)

    return expanding_rows, expanding_cols, galaxies


def transform_galaxies(galaxies, empty_rows, empty_cols, expansion_factor=2):
    new_galaxies = []
    for r, c in galaxies:
        n_rows = len(list(filter(lambda r_index: r_index < r, empty_rows)))
        n_cols = len(list(filter(lambda c_index: c_index < c, empty_cols)))
        new_r = r + n_rows * (expansion_factor - 1)
        new_c = c + n_cols * (expansion_factor - 1)
        new_galaxies.append((new_r, new_c))
    return new_galaxies


def manhattan_distance(galaxy_1, galaxy_2):
    return abs(galaxy_1[0] - galaxy_2[0]) + abs(galaxy_1[1] - galaxy_2[1])


if __name__ == "__main__":
    file_input = read_file("inputs/day11.txt")
    lines = split_lines(file_input)

    answer_1 = 0
    answer_2 = 0

    empty_rows, empty_cols, galaxies = get_grid_information(lines)

    print("Part 1")
    new_galaxies = transform_galaxies(galaxies, empty_rows, empty_cols)

    for i in range(len(new_galaxies)):
        for j in range(i + 1, len(new_galaxies)):
            dist = manhattan_distance(new_galaxies[i], new_galaxies[j])
            answer_1 += dist

    print(answer_1)

    print("Part 2")
    new_galaxies = transform_galaxies(galaxies, empty_rows, empty_cols, 1000000)

    for i in range(len(new_galaxies)):
        for j in range(i + 1, len(new_galaxies)):
            dist = manhattan_distance(new_galaxies[i], new_galaxies[j])
            answer_2 += dist

    print(answer_2)
