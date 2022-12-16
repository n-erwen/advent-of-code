from typing import List


def load_puzzle_input(file_name: str) -> str:
    with open(file_name, "r") as file:
        return file.read().rstrip()


def split_input_rows(input_string: str) -> List[str]:
    return [r for r in input_string.split("\n")]


def split_pair(sect_assignment_pair: str) -> List[str]:
    return sect_assignment_pair.split(',')


def get_sect_assignment_as_range(assignment: str) -> range:
    start, end = [int(num) for num in assignment.split('-')]
    return range(start, end+1)


def does_range_fully_contain_other_range(a: range, b: range) -> bool:
    return set(a).issubset(set(b)) or set(b).issubset(set(a))


def do_ranges_overlap(a: range, b: range) -> bool:
    return not set(a).isdisjoint(set(b))


def part1_solution(sect_assignment_pairs: List[str]) -> int:
    num_pairs_containing = 0
    for p in sect_assignment_pairs:
        a, b = [get_sect_assignment_as_range(s) for s in split_pair(p)]
        if does_range_fully_contain_other_range(a, b):
            num_pairs_containing += 1
    return num_pairs_containing


def part2_solution(sect_assignment_pairs: List[str]) -> int:
    num_pairs_containing = 0
    for p in sect_assignment_pairs:
        a, b = [get_sect_assignment_as_range(s) for s in split_pair(p)]
        if do_ranges_overlap(a, b):
            num_pairs_containing += 1
    return num_pairs_containing


if __name__ == "__main__":
    puzzle_input = split_input_rows(load_puzzle_input("./input.txt"))
    print(f"Part 1 Solution: {part1_solution(puzzle_input)}")
    print(f"Part 2 Solution: {part2_solution(puzzle_input)}")
