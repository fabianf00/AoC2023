def read_file(file_name) -> str:
    with open(file_name) as f:
        return f.read().rstrip()


def get_first_number(line) -> int:
    for char in line:
        if char.isdigit():
            return int(char)


def part1(input):
    lines = input.split("\n")
    calibration_values = []
    for line in lines:
        first_digit = get_first_number(line)
        second_digit = get_first_number(line[::-1])
        calibration_values.append(first_digit * 10 + second_digit)
    return sum(calibration_values)


input = read_file("part_1.txt")

result = part1(input)

print(result)
