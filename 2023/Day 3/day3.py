import string


def load_puzzle_input(file_name: str) -> str:
    with open(file_name, "r") as file:
        return file.read().rstrip()


def is_non_period_symbol(char: str) -> bool:
    return char in string.punctuation and char != "."


def get_adjacent_coordinates(row_index: int, column_index: int, num_rows: int, num_columns: int) -> [(int, int)]:
    coordinates_list = [
        (row_index - 1, column_index - 1),   # NORTHWEST
        (row_index - 1, column_index),       # NORTH
        (row_index - 1, column_index + 1),   # NORTHEAST
        (row_index, column_index + 1),       # EAST
        (row_index + 1, column_index + 1),  # SOUTHEAST
        (row_index + 1, column_index),       # SOUTH
        (row_index + 1, column_index - 1),   # SOUTHWEST
        (row_index, column_index - 1)        # WEST
    ]
    return [
        coordinates for coordinates in coordinates_list
        if (coordinates[0] in range(num_rows) and coordinates[1] in range(num_columns))
    ]


def is_part_num(schematic_grid: [[str]], row_index: int, column_index: int) -> bool:
    adjacent_coordinates = get_adjacent_coordinates(row_index, column_index, len(schematic_grid), len(schematic_grid[0]))
    for coordinates in adjacent_coordinates:
        if is_non_period_symbol(schematic_grid[coordinates[0]][coordinates[1]]):
            return True
    return False


def part1_solution(puzzle_input: str) -> int:
    schematic_grid = [list(row) for row in puzzle_input.split("\n")]

    for row_index in range(len(schematic_grid[0])):
        for column_index in range(len(schematic_grid[0])):
            char = schematic_grid[row_index][column_index]
            if char.isnumeric():
                print(char, row_index, column_index, is_part_num(schematic_grid, row_index, column_index))

    return -1


def part2_solution(puzzle_input: str) -> int:
    return -1


if __name__ == "__main__":
    day3_puzzle_input = load_puzzle_input("./input.txt")
    print(f"(Day 3 Part 1) Solution: {part1_solution(day3_puzzle_input)}")
    print(f"(Day 3 Part 2) Solution: {part2_solution(day3_puzzle_input)}")
