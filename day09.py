from utils import read_file, split_lines
import re


def get_substract_list(sequence):
    substract_list = []

    for i in range(len(sequence) - 1):
        substract_list.append(sequence[i + 1] - sequence[i])

    return substract_list


def is_zero_sequence(sequence):
    for number in sequence:
        if number != 0:
            return False

    return True


def create_diffence_sequence_pyramid(sequence):
    matrix = [sequence.copy()]
    while not is_zero_sequence(matrix[-1]):
        substract_list = get_substract_list(matrix[-1])
        matrix.append(substract_list)

    return matrix


def predict_next_number(sequence):
    sequence_lists = create_diffence_sequence_pyramid(sequence)

    prev = 0
    for number_sequence in sequence_lists[::-1]:
        number = number_sequence[-1] + prev
        prev = number

    return prev


def predict_previous_number(sequence):
    sequence_lists = create_diffence_sequence_pyramid(sequence)

    prev = 0
    for number_sequence in sequence_lists[::-1]:
        prev = number_sequence[0] - prev

    return prev


if __name__ == "__main__":
    file_input = read_file("inputs/day09.txt")
    lines = split_lines(file_input)

    sequences = []

    for line in lines:
        sequences.append(
            list(map(lambda number: int(number), re.findall(r"(-?\d+)", line)))
        )

    answer_1, answer_2 = 0, 0
    print("Part 1")
    for sequence in sequences:
        answer_1 += predict_next_number(sequence)
    print(answer_1)
    print("Part 2")
    for sequence in sequences:
        answer_2 += predict_previous_number(sequence)

    print(answer_2)
