from utils import read_file, split_lines
import re
from collections import deque


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


def count_inside_circle(grid, circle):
    count = 0
    for r, row in enumerate(grid):
        inside_circle = False
        for c, label in enumerate(row):
            if (r, c) not in circle:
                if inside_circle:
                    count += 1
            elif label in "|F7S":
                inside_circle = not inside_circle

    return count


if __name__ == "__main__":
    file_input = read_file("inputs/day10.txt")
    grid = split_lines(file_input)

    answer_1 = 0
    starting_point = None

    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col == "S":
                starting_point = (r, c)
                break

    print("Part 1")
    circle = get_circle(grid, *starting_point)

    answer_1 = len(circle) // 2
    print(answer_1)

    print("Part 2")
    answer_2 = count_inside_circle(grid, circle)
    print(answer_2)
