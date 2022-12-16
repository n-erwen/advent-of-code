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


def group_elves(rucksacks: List[str]) -> List[List[str]]:
    return [rucksacks[index:index+3] for index in range(0, len(rucksacks), 3)]


def get_shared_item_types(sets: List[set[str]]) -> List[str]:
    return [item for item in set.intersection(*sets)]


def get_item_priority_value(item: str) -> int:
    return ascii_letters.index(item) + 1


def get_priority_total(items: List[str]) -> int:
    return sum(get_item_priority_value(i) for i in items)


def part1_solution(rucksacks: List[str]) -> int:
    """Part 1: Find the item type that appears in both compartments of each rucksack.
    What is the sum of the priorities of those item types?"""
    shared_item_types = sum([
        get_shared_item_types([set(c) for c in split_compartments(r)])
        for r in rucksacks
    ], [])
    return get_priority_total(shared_item_types)


def part2_solution(rucksacks: List[str]) -> int:
    """Part 2:"""
    shared_item_types = sum(
        [get_shared_item_types([set(g) for g in grp])
         for grp in group_elves(rucksacks)], []
    )
    return get_priority_total(shared_item_types)


if __name__ == "__main__":
    rucksacks_input = split_rucksacks(load_puzzle_input("./input.txt"))
    print(f"Part 1 Solution: {part1_solution(rucksacks_input)}")
    print(f"Part 2 Solution: {part2_solution(rucksacks_input)}")
