def load_puzzle_input(file_name: str) -> str:
    with open(file_name, "r") as file:
        return file.read().rstrip()


def generate_file_tree(command_output: str):
    command_strings = command_output.lstrip("$ ").split("$ ")
    for command_string in command_strings:
        print(command_string)
        print("\n")
    return None


def part1_solution(puzzle_input: str) -> None:
    file_tree = generate_file_tree(puzzle_input)
    return None


def part2_solution(puzzle_input: str) -> None:
    return None


if __name__ == "__main__":
    day7_puzzle_input = load_puzzle_input("./input.txt")
    print(f"(Day 7 Part 1): {part1_solution(day7_puzzle_input)}")
    print(f"(Day 7 Part 2): {part2_solution(day7_puzzle_input)}")
