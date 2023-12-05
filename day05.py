from utils import read_file, split_lines
import re


def transform_mappings(mappings):
    # remove the first line of each mapping and split by line
    string_values_list = list(map(lambda x: x.split(":")[1].split("\n")[1:], mappings))

    # convert string of numbers in list of numbers
    for i in range(len(string_values_list)):
        string_values_list[i] = list(
            map(
                lambda x: list(map(lambda value: int(value), x.split(" "))),
                string_values_list[i],
            )
        )

    return string_values_list


def get_mapped_value(mappings, original_value):
    # check if the seed is in the range of the mapping
    # if it is then use the mapping to transform the seed
    # if it is not in range then continue to the next mapping
    # if in no mapping range then the mapping is equal to the seed
    for mapping in mappings:
        if mapping[1] > original_value:
            break
        if original_value < mapping[1] + mapping[2]:
            return mapping[0] + (original_value - mapping[1])
    return original_value


if __name__ == "__main__":
    file_input = read_file("inputs/day05.txt")

    seeds, *mappings_list = file_input.split("\n\n")
    answer_1 = 0
    answer_2 = 0

    print("--- Part 1 ---")
    seeds = list(map(lambda x: int(x), re.findall(r"(\d+)", seeds)))
    mapping_results = seeds.copy()
    mappings_list = transform_mappings(mappings_list)

    # sort the mappings by source mapping
    for i in range(len(mappings_list)):
        mappings_list[i].sort(key=lambda x: x[1])

    for seed_index in range(len(seeds)):
        for mappings in mappings_list:
            mapping_results[seed_index] = get_mapped_value(
                mappings, mapping_results[seed_index]
            )
    min = 0
    for i in range(1, len(mapping_results)):
        if mapping_results[i] < mapping_results[min]:
            min = i
    answer_1 = mapping_results[min]

    print(f"Answer 1: {answer_1}")
    print("--- Part 2 ---")
    answer_2 = float("inf")
    for i in range(0, len(seeds), 2):
        for seed in range(seeds[i], seeds[i] + seeds[i + 1]):
            value = seed
            for mappings in mappings_list:
                value = get_mapped_value(mappings, value)

            if value < answer_2:
                answer_2 = value

    print(f"Answer 2: {answer_2}")
