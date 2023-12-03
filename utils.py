def read_file(file_name) -> str:
    with open(file_name) as f:
        return f.read().rstrip()


def split_lines(input) -> list:
    return input.split("\n")
