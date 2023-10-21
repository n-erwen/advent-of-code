import re
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='\n%(levelname)s - %(asctime)s\n'
           + '-' * 31
           + '\n%(message)s\n'
           + '-' * 31 + '\n')


def load_puzzle_input(file_name: str) -> str:
    with open(file_name, "r") as file:
        return file.read().rstrip()


def get_num_columns(stacks):
    return len(stacks.split("\n")[-1].split())


def get_crates(stack_row):
    crate_regex = r'\[[A-Z]\]'
    return re.findall(crate_regex, stack_row)


def parse_stack_drawing(stack_drawing):
    stack_array = []
    stack_numbers = stack_drawing.split("\n")[-1].strip().split()
    logging.debug(stack_numbers)
    for row in stack_drawing.split("\n")[:-1]:
        stack_array.append([])
    return []


def part1_solution(puzzle_input: str) -> str:
    stacks_drawing, procedure = puzzle_input.split("\n\n")
    logging.debug(stacks_drawing)
    parse_stack_drawing(stacks_drawing)
    return ""


def part2_solution(puzzle_input):
    return ""


if __name__ == "__main__":
    day5_puzzle_input = load_puzzle_input("./input.txt")
    print(f"(Day 5 Part 1) Crates on top of each stack: {part1_solution(day5_puzzle_input)}")
    print(f"(Day 5 Part 2): {part2_solution(day5_puzzle_input)}")
