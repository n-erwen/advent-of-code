from lib import load_puzzle_input


def convert_column_to_list(puzzle_input: str, column_index) -> list[int]:
    return [int(row.split("   ")[column_index]) for row in puzzle_input.split('\n')]


def part1_solution(puzzle_input: str) -> int:
    left_list = sorted(convert_column_to_list(puzzle_input, 0))
    right_list = sorted(convert_column_to_list(puzzle_input, 1))

    return sum(abs(left_list[i] - right_list[i]) for i in range(len(left_list)))


def part2_solution(puzzle_input: str) -> int:
    left_list = convert_column_to_list(puzzle_input, 0)
    right_list = convert_column_to_list(puzzle_input, 1)

    return sum(num * right_list.count(num) for num in left_list)


if __name__ == "__main__":
    day1_puzzle_input = load_puzzle_input("./input.txt")
    print(f"Day 1 Part 1 Solution: {part1_solution(day1_puzzle_input)}")
    print(f"Day 1 Part 2 Solution: {part2_solution(day1_puzzle_input)}")