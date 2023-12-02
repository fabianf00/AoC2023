import re


def read_file(file_name) -> str:
    with open(file_name) as f:
        return f.read().rstrip()


def split_lines(input) -> list:
    return input.split("\n")


def get_maximum_colors(sets):
    max_red = max(
        map(lambda result: int(result.split(" ")[0]), re.findall(r"\d+ red", sets))
    )
    max_green = max(
        map(lambda result: int(result.split(" ")[0]), re.findall(r"\d+ green", sets))
    )
    max_blue = max(
        map(lambda result: int(result.split(" ")[0]), re.findall(r"\d+ blue", sets))
    )

    return max_red, max_green, max_blue


def part1(lines, red=12, green=13, blue=14):
    id_sum = 0
    for line in lines:
        _, sets = line.split(":")

        game_id = int(re.findall(r"\d+", line)[0])
        used_red, used_green, used_blue = get_maximum_colors(sets)

        if used_red <= red and used_green <= green and used_blue <= blue:
            id_sum += game_id
    return id_sum


def part2(lines):
    power_sum = 0
    for line in lines:
        _, sets = line.split(":")
        # minimum as in minimum needed to get results
        minimum_red, minimum_green, minimum_blue = get_maximum_colors(sets)

        power_sum += minimum_red * minimum_green * minimum_blue
    return power_sum


input = read_file("input.txt")

print("--- Part One ---")
print(part1(split_lines(input)))
print("--- Part Two ---")
print(part2(split_lines(input)))
