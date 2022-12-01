from typing import List


def load_puzzle_input(file_name: str) -> str:
    with open(file_name, "r") as file:
        return file.read().rstrip()


def split_inventories(input_string: str) -> List[List[int]]:
    return [[int(calories) for calories in inv.split("\n")] for inv in input_string.split("\n\n")]


def get_calorie_counts(inventories: List[List[int]]) -> List[int]:
    return [sum(inv) for inv in inventories]


def part1_solution(inventories: List[List[int]]) -> int:
    """Part 1: Total calories the elf with the most calories is carrying"""
    return max(get_calorie_counts(inventories))


def part2_solution(inventories: List[List[int]]) -> int:
    """Part 2: Sum of calories the top three elves are carrying"""
    return sum(sorted(get_calorie_counts(inventories), reverse=True)[:3])


if __name__ == "__main__":
    inventories_input = split_inventories(load_puzzle_input("./input.txt"))
    print(f"Part 1 Solution: {part1_solution(inventories_input)}")
    print(f"Part 2 Solution: {part2_solution(inventories_input)}")
