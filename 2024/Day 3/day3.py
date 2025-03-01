from lib import load_puzzle_input
import re


def get_mul_instructions(puzzle_input: str) -> [str]:
    mul_regex = r'(mul\(\d+,\d+\))'
    return re.findall(mul_regex, puzzle_input)


def get_all_instructions(puzzle_input: str) -> [str]:
    instruction_regex = r'mul\(\d+,\d+\)|don\'t\(\)|do\(\)'
    return re.findall(instruction_regex, puzzle_input)


def get_mul_operands(instruction: str) -> [int, int]:
    operand_regex = r'mul\((\d+),(\d+)\)'
    matched_operands = re.match(operand_regex, instruction).groups()
    return [int(matched_operands[0]), int(matched_operands[1])]


def multiply(num_1: int, num_2: int) -> int:
    return num_1 * num_2


def part1_solution(puzzle_input: str) -> int:
    puzzle_input_no_newlines = puzzle_input.replace('\n', '')
    return sum(
        multiply(*get_mul_operands(mul_instruction))
        for mul_instruction in get_mul_instructions(puzzle_input_no_newlines)
    )


def part2_solution(puzzle_input: str) -> int:
    puzzle_input_no_newlines = puzzle_input.replace('\n', '')
    all_instructions = get_all_instructions(puzzle_input_no_newlines)
    enabled_mul_total = 0
    skip_mul = False

    for instruction in all_instructions:
        if instruction == 'don\'t()':
            skip_mul = True
        elif instruction == 'do()':
            skip_mul = False
        elif instruction.startswith('mul') and not skip_mul:
            enabled_mul_total += multiply(*get_mul_operands(instruction))

    return enabled_mul_total


if __name__ == "__main__":
    day3_puzzle_input = load_puzzle_input("./input.txt")
    print(f"Day 3 Part 1 Solution: {part1_solution(day3_puzzle_input)}")
    print(f"Day 3 Part 2 Solution: {part2_solution(day3_puzzle_input)}")
