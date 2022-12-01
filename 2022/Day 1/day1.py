from typing import List


def load_puzzle_input(file_name: str) -> str:
    with open(file_name, "r") as file:
        return file.read().rstrip()


def split_inventories(input_string: str) -> List[List[int]]:
    return [[int(calories) for calories in inv.split("\n")] for inv in input_string.split("\n\n")]


def part1_solution(input_string: str) -> int:
    """Part 1: Total calories the elf with the most calories is carrying"""
    calorie_counts = [sum(inv) for inv in split_inventories(input_string)]
    return max(calorie_counts)


def part2_solution(input_string: str) -> int:
    """Part 2: Sum of calories the top three elves are carrying"""
    calorie_counts = [sum(inv) for inv in split_inventories(input_string)]
    top_three_calories = sorted(calorie_counts, reverse=True)[:3]
    return sum(top_three_calories)


if __name__ == "__main__":
    input_string = load_puzzle_input("./input.txt")
    print(f"Part 1 Solution: {part1_solution(input_string)}")
    print(f"Part 2 Solution: {part2_solution(input_string)}")
