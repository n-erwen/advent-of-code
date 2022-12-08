from typing import List
from string import ascii_letters


def load_puzzle_input(file_name: str) -> str:
    with open(file_name, "r") as file:
        return file.read().rstrip()


def split_rucksacks(input_string: str) -> List[str]:
    return [r for r in input_string.split("\n")]


def split_compartments(rucksack: str) -> tuple[str, str]:
    mid_index = (len(rucksack) // 2)
    return rucksack[:mid_index], rucksack[mid_index:]


def part1_solution(rucksacks: List[str]) -> int:
    """Part 1: Find the item type that appears in both compartments of each rucksack.
    What is the sum of the priorities of those item types?"""
    shared_item_types = []
    for r in rucksacks:
        compartment_sets = [set(c) for c in split_compartments(r)]
        for item in compartment_sets[0].intersection(compartment_sets[1]):
            shared_item_types.append(item)
    return sum([ascii_letters.index(letter) + 1 for letter in shared_item_types])


def part2_solution(game_rounds: List[str]) -> int:
    """Part 2:"""
    return 0


if __name__ == "__main__":
    rucksacks_input = split_rucksacks(load_puzzle_input("./input.txt"))
    print(f"Part 1 Solution: {part1_solution(rucksacks_input)}")
    print(f"Part 2 Solution: {part2_solution(rucksacks_input)}")
