import re


def load_puzzle_input(file_name: str) -> str:
    with open(file_name, "r") as file:
        return file.read().rstrip()


def get_num_stacks(stack_drawing):
    return len(stack_drawing.split("\n")[-1].strip().split())


def parse_instruction(instruction):
    operands = [int(operand) for operand in re.findall(r'[0-9]+', instruction)]
    return {"quantity": operands[0], "from_index": operands[1] - 1, "to_index": operands[2] - 1}


def parse_stack_drawing(stack_drawing):
    stack_array = [[] for _ in range(get_num_stacks(stack_drawing))]
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
        crate = stacks[instruc["from_index"]].pop(0)
        stacks[instruc["to_index"]].insert(0, crate)
    return stacks


def move_multi_crates(stacks, instruc):
    crates = stacks[instruc["from_index"]][0:instruc["quantity"]]
    del stacks[instruc["from_index"]][0:instruc["quantity"]]
    stacks[instruc["to_index"]] = crates + stacks[instruc["to_index"]]
    return stacks


def get_crate_letter(crate):
    return re.search(r"[A-Z]", crate).group()


def parse_puzzle_input(puzzle_input):
    stacks_drawing, procedure_string = puzzle_input.split("\n\n")
    stack_array = parse_stack_drawing(stacks_drawing)
    procedure_array = [parse_instruction(instruc) for instruc in procedure_string.split("\n")]
    return stack_array, procedure_array


def part1_solution(puzzle_input: str) -> str:
    stack_array, procedure_array = parse_puzzle_input(puzzle_input)
    for instruc in procedure_array:
        stack_array = move_crates(stack_array, instruc)
    return "".join([get_crate_letter(stack[0]) for stack in stack_array])


def part2_solution(puzzle_input):
    stack_array, procedure_array = parse_puzzle_input(puzzle_input)
    for instruc in procedure_array:
        stack_array = move_multi_crates(stack_array, instruc)
    return "".join([get_crate_letter(stack[0]) if stack else "" for stack in stack_array])


if __name__ == "__main__":
    day5_puzzle_input = load_puzzle_input("./input.txt")
    print(f"(Day 5 Part 1) Crates on top of each stack: {part1_solution(day5_puzzle_input)}")
    print(f"(Day 5 Part 2) Crates on top of each stack: {part2_solution(day5_puzzle_input)}")
