from lib import load_puzzle_input


def convert_input_to_report_lists(puzzle_input: str) -> list[list[int]]:
    return [[int(level) for level in report.split(" ")] for report in puzzle_input.split("\n")]


def are_levels_increasing(report: list[int]) -> bool:
    return all(report[i] > report[i-1] for i in range(1, len(report)))


def are_levels_decreasing(report: list[int]) -> bool:
    return all(report[i] < report[i-1] for i in range(1, len(report)))

def are_all_level_differences_safe(report: list[int]) -> bool:
    return all(1 <= abs(report[i] - report[i-1]) <= 3 for i in range(1, len(report)))


def is_report_safe(report: list[int]):
    return (are_levels_increasing(report) or are_levels_decreasing(report)) and are_all_level_differences_safe(report)


def is_report_safe_with_problem_dampener(report: list[int]):
    return any([
        is_report_safe([report[i] for i in range(len(report)) if i != index_to_remove])
        for index_to_remove in range(len(report))
    ])


def part1_solution(puzzle_input: str) -> int:
    reports = convert_input_to_report_lists(puzzle_input)
    return [is_report_safe(report) for report in reports].count(True)


def part2_solution(puzzle_input: str) -> int:
    reports = convert_input_to_report_lists(puzzle_input)
    return [is_report_safe_with_problem_dampener(report) for report in reports].count(True)


if __name__ == "__main__":
    day1_puzzle_input = load_puzzle_input("./input.txt")
    print(f"Day 2 Part 1 Solution: {part1_solution(day1_puzzle_input)}")
    print(f"Day 2 Part 2 Solution: {part2_solution(day1_puzzle_input)}")
