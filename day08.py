from utils import read_file, split_lines
import re
from math import lcm


def parse_network_string(network_string_list):
    network = {}

    for line in network_string_list:
        node, neigbors = line.split(" = ")
        network[node] = tuple(re.findall(r"\w+", neigbors))
    return network


def get_next_direction(directions):
    i = 0
    while True:
        yield directions[i]
        i = (i + 1) % len(directions)


if __name__ == "__main__":
    file_input = read_file("inputs/day08.txt")
    directions, _, *network = split_lines(file_input)

    network_dict = parse_network_string(network)
    answer_1, answer_2 = 0, 0

    print("Part 1")
    node = "AAA"
    for direction in get_next_direction(directions):
        answer_1 += 1
        if direction == "L":
            node = network_dict[node][0]
        elif direction == "R":
            node = network_dict[node][1]

        if node == "ZZZ":
            break
    print(answer_1)

    print("Part 2")
    nodes = list(filter(lambda string: string.endswith("A"), network_dict.keys()))
    operations = []
    for node in nodes:
        nr_operations = 0
        for direction in get_next_direction(directions):
            nr_operations += 1
            if direction == "L":
                node = network_dict[node][0]
            elif direction == "R":
                node = network_dict[node][1]

            if node[-1] == "Z":
                operations.append(nr_operations)
                break

    answer_2 = lcm(*operations)

    print(answer_2)
