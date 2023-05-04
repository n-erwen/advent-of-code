def read_input_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        return file.read().rstrip()


def intcode_add(program: list[int], pos: int):
    program[program[pos+3]] = program[program[pos+1]] + program[program[pos+2]]


def intcode_multiply(program: list[int], pos: int):
    program[program[pos+3]] = program[program[pos+1]] * program[program[pos+2]]


def run_intcode_program(program: list[int]):
    n = 0
    while program[n] != 99:
        if program[n] == 1:
            intcode_add(program, n)
        elif program[n] == 2:
            intcode_multiply(program, n)
        n += 4
    return program


def modify_program_pos1_and_pos2(program: list[int], pos1_value: int, pos2_value: int):
    program[1] = pos1_value
    program[2] = pos2_value
    return program


def modify_and_run_intcode_program(program: list[int], pos1: int, pos2: int) -> int:
    return run_intcode_program(modify_program_pos1_and_pos2(program, pos1, pos2))[0]


def get_valid_noun_verb_pair_for_target(program: list[int], target: int) -> [int, int]:
    for noun in range(100):
        verb_99_output = modify_and_run_intcode_program(program.copy(), noun, 99)
        if verb_99_output == target:
            return [noun, 99]
        elif verb_99_output > target:
            for verb in range(99):
                output = modify_and_run_intcode_program(program.copy(), noun, verb)
                if output == target:
                    return [noun, verb]
    return [-1, -1]


def part1_solution(program: list[int]) -> int:
    return modify_and_run_intcode_program(program, 12, 2)


def part2_solution(program: list[int]):
    noun, verb = get_valid_noun_verb_pair_for_target(program, 19690720)
    return 100 * noun + verb


if __name__ == "__main__":
    intcode_program = [int(i) for i in read_input_file("input.txt").split(",")]

    part1_result = part1_solution(intcode_program.copy())
    print("Part 1 Result: {}".format(part1_result))

    part2_result = part2_solution(intcode_program.copy())
    print("Part 2 Result: {}".format(part2_result))
