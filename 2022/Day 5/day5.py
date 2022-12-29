import re


def load_puzzle_input(file_name: str) -> str:
    with open(file_name, "r") as file:
        return file.read().rstrip()


def get_num_columns(stacks):
    return len(stacks.split("\n")[-1].split())


def get_crates(stack_row):
    crate_regex = r'\[[A-Z]\]'
    return re.findall(crate_regex, stack_row)


def part1_solution(puzzle_input: str) -> str:
    stacks_drawing, procedure = puzzle_input.split("\n\n")
    print([get_crates(s) for s in stacks_drawing.split('\n')[:-1]])
    return ""


def part2_solution(puzzle_input):
    return ""


if __name__ == "__main__":
    puzzle_input = load_puzzle_input("./input.txt")
    print(f"Part 1 Solution: {part1_solution(puzzle_input)}")
    print(f"Part 2 Solution: {part2_solution(puzzle_input)}")
