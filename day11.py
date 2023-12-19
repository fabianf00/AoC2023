from utils import read_file, split_lines
import re


def expand_grid(grid, multiplier=2):
    new_grid = []
    row_count = [0 for _ in range(len(lines))]
    col_count = [0 for _ in range(len(lines[0]))]

    for r, row in enumerate(lines):
        for c, col in enumerate(row):
            if col == "#":
                row_count[r] += 1
                col_count[c] += 1

    for r, row in enumerate(grid):
        new_row = []
        for c, col in enumerate(row):
            new_row.append(col)
            if col_count[c] == 0:
                new_row.append(".")
        new_grid.append(new_row)
        if row_count[r] == 0:
            new_grid.append(new_row)

    return new_grid


def shortest_distance(galaxy_1, galaxy_2):
    return abs(galaxy_1[0] - galaxy_2[0]) + abs(galaxy_1[1] - galaxy_2[1])


if __name__ == "__main__":
    file_input = read_file("inputs/day11.txt")
    lines = split_lines(file_input)

    answer_1 = 0
    answer_2 = 0

    print("Part 1")
    grid = expand_grid(lines)
    galaxies = []

    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col == "#":
                galaxies.append((r, c))

    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            dist = shortest_distance(galaxies[i], galaxies[j])
            answer_1 += dist

    print(answer_1)

    print("Part 2")
