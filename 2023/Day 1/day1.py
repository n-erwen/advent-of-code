import re

NUMBER_WORDS = ["one", "two", "three", "four",
                "five", "six", "seven", "eight", "nine"]


def convert_to_numeral(number_word: str) -> str:
    return str(NUMBER_WORDS.index(number_word) + 1)


def load_puzzle_input(file_name: str) -> str:
    with open(file_name, "r") as file:
        return file.read().rstrip()


def get_calibration_value(line: str, number_search_string: str) -> int:
    numbers = re.findall(number_search_string, line)
    if len(numbers):
        calibration_digits = [
            num if num.isnumeric() else convert_to_numeral(num)
            for num in [numbers[0], numbers[-1]]
        ]
        return int("".join(calibration_digits))

    return 0


def part1_solution(puzzle_input: str) -> int:
    lines = puzzle_input.split("\n")
    return sum([
        get_calibration_value(line, r"[1-9]{1}")
        for line in lines
    ])


def part2_solution(puzzle_input: str) -> int:
    """Solved with help from https://www.reddit.com/r/adventofcode/comments/18c1ecd/aoc_2023_day_1_part_2/"""
    lines = puzzle_input.split("\n")
    return sum([
        get_calibration_value(
            line, rf"(?=([1-9]|{'|'.join(NUMBER_WORDS)})){{1}}")
        for line in lines
    ])


if __name__ == "__main__":
    day1_puzzle_input = load_puzzle_input("./input.txt")
    print(f"(Day 1 Part 1) Solution: {part1_solution(day1_puzzle_input)}")
    print(f"(Day 1 Part 2) Solution: {part2_solution(day1_puzzle_input)}")
