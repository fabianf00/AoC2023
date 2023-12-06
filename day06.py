from utils import read_file, split_lines
import re


def count_winning_ways(time, distance):
    number_winnings = 0
    for i in range(1, time):
        if (time - i) * i > distance:
            number_winnings += 1
    return number_winnings


if __name__ == "__main__":
    file_input = read_file("inputs/day06.txt")

    lines = split_lines(file_input)

    answer_1, answer_2 = 1, 0

    print("Part 1")
    times = list(map(lambda time: int(time), re.findall(r"\d+", lines[0])))
    distances = list(map(lambda distance: int(distance), re.findall(r"\d+", lines[1])))

    for time, distance in zip(times, distances):
        answer_1 *= count_winning_ways(time, distance)
    print(answer_1)
    print("Part 2")
    time = int("".join(list(map(lambda t: str(t), times))))
    distance = int("".join(list(map(lambda dist: str(dist), distances))))
    answer_2 = count_winning_ways(time, distance)
    print(answer_2)
