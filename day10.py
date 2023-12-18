from utils import read_file, split_lines
import re
from collections import deque

"""

    | is a vertical pipe connecting north and south.
    - is a horizontal pipe connecting east and west.
    L is a 90-degree bend connecting north and east.
    J is a 90-degree bend connecting north and west.
    7 is a 90-degree bend connecting south and west.
    F is a 90-degree bend connecting south and east.
    . is ground; there is no pipe in this tile.
    S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

"""


def check_coordinates(grid, *points):
    max_row = len(grid) - 1
    max_col = len(grid[0]) - 1

    for r, c in points:
        if r >= 0 and r <= max_row and c >= 0 and c <= max_col:
            yield r, c


def get_starting_point_neighbors(grid, r, c):
    starting_neighbors = []
    if grid[r + 1][c] in "|LJ":
        starting_neighbors.append((r + 1, c))

    if grid[r - 1][c] in "|F7":
        starting_neighbors.append((r - 1, c))

    if grid[r][c - 1] in "-LF":
        starting_neighbors.append((r, c - 1))

    if grid[r][c + 1] in "-J7":
        starting_neighbors.append((r, c + 1))

    return starting_neighbors


def get_neighbors(grid, r, c):
    if grid[r][c] == "|":
        return check_coordinates(grid, (r - 1, c), (r + 1, c))
    elif grid[r][c] == "-":
        return check_coordinates(grid, (r, c - 1), (r, c + 1))
    elif grid[r][c] == "L":
        return check_coordinates(grid, (r - 1, c), (r, c + 1))
    elif grid[r][c] == "J":
        return check_coordinates(grid, (r - 1, c), (r, c - 1))
    elif grid[r][c] == "7":
        return check_coordinates(grid, (r + 1, c), (r, c - 1))
    elif grid[r][c] == "F":
        return check_coordinates(grid, (r + 1, c), (r, c + 1))
    elif grid[r][c] == "S":
        return check_coordinates(grid, *get_starting_point_neighbors(grid, r, c))


def get_circle(grid, starting_row, starting_col):
    seen = set()
    queue = deque()

    queue.append((starting_row, starting_col))

    while queue:
        r, c = queue.popleft()
        if (r, c) not in seen:
            seen.add((r, c))
            for neighbor in get_neighbors(grid, r, c):
                queue.append(neighbor)

    return seen


if __name__ == "__main__":
    file_input = read_file("inputs/day10.txt")
    grid = split_lines(file_input)

    answer_1 = 0

    print("Part 1")

    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col == "S":
                answer_1 = len(get_circle(grid, r, c)) // 2
                break
    print(answer_1)

    print("Part 2")
    answer_2 = 0
