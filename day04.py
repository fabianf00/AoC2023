from utils import read_file, split_lines
import re


def get_numbers(line):
    wining_numbers, numbers = line.split("|")
    wining_numbers_list = list(
        map(lambda x: int(x), re.findall(r"\d+", wining_numbers))
    )
    numbers_list = list(map(lambda x: int(x), re.findall(r"\d+", numbers)))

    return wining_numbers_list, numbers_list


def count_matching_numbers(wining_numbers, numbers):
    filtered_numbers = list(filter(lambda x: x in wining_numbers, numbers))
    return len(filtered_numbers)


if __name__ == "__main__":
    file_input = read_file("inputs/day04.txt")
    lines = split_lines(file_input)

    answer_1 = 0
    answer_2 = 0

    print("--- Part 1 ---")
    for line in lines:
        card_id, numbers = line.split(":")
        card_id = int(re.findall(r"\d+", card_id)[0])
        wining_numbers, numbers = get_numbers(numbers)
        count_matching = count_matching_numbers(wining_numbers, numbers)
        if count_matching == 0:
            continue
        points = pow(2, count_matching - 1)
        answer_1 += points

    print(f"Answer 1: {answer_1}")
    print("--- Part 2 ---")
    list_card_distribution = [1 for _ in range(len(lines))]

    for index, line in enumerate(lines):
        numbers = line.split(":")[1]
        wining_numbers, numbers = get_numbers(numbers)
        count_matching = count_matching_numbers(wining_numbers, numbers)
        if count_matching == 0:
            continue
        for i in range(1, count_matching + 1):
            list_card_distribution[index + i] += list_card_distribution[index]

    answer_2 = sum(list_card_distribution)
    print(f"Answer 2: {answer_2}")
