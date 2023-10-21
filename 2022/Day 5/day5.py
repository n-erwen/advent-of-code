import re
import logging
from collections import deque

logging.basicConfig(
    level=logging.INFO,
    format='\n%(levelname)s - %(asctime)s\n'
           + '-' * 31
           + '\n%(message)s\n'
           + '-' * 31 + '\n'
)


def load_puzzle_input(file_name: str) -> str:
    with open(file_name, "r") as file:
        return file.read().rstrip()


def get_num_stacks(stack_drawing):
    return len(stack_drawing.split("\n")[-1].strip().split())


def parse_instruction(instruction):
    operands = [int(operand) for operand in re.findall(r'[0-9]+', instruction)]
    return {"quantity": operands[0], "from_stack": operands[1], "to_stack": operands[2]}


def parse_stack_drawing(stack_drawing):
    stack_array = deque([deque([]) for _ in range(get_num_stacks(stack_drawing))])
    for row in stack_drawing.split("\n")[:-1]:
        stack_index = 0
        for i in range(0, len(row), 4):
            crate = row[i:i+3]
            if crate.strip():
                stack_array[stack_index].append(crate)
            stack_index += 1
    return stack_array


def move_crates(stacks, instruc):
    for _ in range(instruc["quantity"]):
        crate = stacks[instruc["from_stack"]-1].popleft()
        stacks[instruc["to_stack"]-1].appendleft(crate)
    return stacks


def get_crate_letter(crate):
    return re.search(r"[A-Z]", crate).group()


def part1_solution(puzzle_input: str) -> str:
    stacks_drawing, procedure_string = puzzle_input.split("\n\n")
    stack_array = parse_stack_drawing(stacks_drawing)
    procedure_array = [parse_instruction(instruc) for instruc in procedure_string.split("\n")]
    for instruc in procedure_array:
        move_crates(stack_array, instruc)
    return "".join([get_crate_letter(stack[0]) for stack in stack_array])


def part2_solution(puzzle_input):
    return ""


if __name__ == "__main__":
    day5_puzzle_input = load_puzzle_input("./input.txt")
    print(f"(Day 5 Part 1) Crates on top of each stack: {part1_solution(day5_puzzle_input)}")
    print(f"(Day 5 Part 2): {part2_solution(day5_puzzle_input)}")
