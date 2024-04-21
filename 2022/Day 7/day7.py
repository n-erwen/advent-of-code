import re


class Folder:
    def __init__(self, parent: "Folder" or None, name=""):
        self.name = name
        self.parent = parent
        self.children = []


class File:
    def __init__(self, size: int, folder: Folder, name=""):
        self.name = name
        self.size = size
        self.folder = folder


def load_puzzle_input(file_name: str) -> str:
    with open(file_name, "r") as file:
        return file.read().rstrip()


def generate_file_tree(terminal_output: str):
    # file_tree = Folder(None, "/")
    # current_node = file_tree
    # print(terminal_output)
    sections = re.findall(r"^\$([\s\S]*?)(?=\$)", terminal_output)
    print(sections)
    return None


def part1_solution(puzzle_input: str) -> None:
    generate_file_tree(puzzle_input)
    return None


def part2_solution(puzzle_input: str) -> None:
    return None


if __name__ == "__main__":
    day7_puzzle_input = load_puzzle_input("./input.txt")
    print(f"(Day 7 Part 1): {part1_solution(day7_puzzle_input)}")
    print(f"(Day 7 Part 2): {part2_solution(day7_puzzle_input)}")
