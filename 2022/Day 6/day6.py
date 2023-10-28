def load_puzzle_input(file_name: str) -> str:
    with open(file_name, "r") as file:
        return file.read().rstrip()


def are_all_chars_unique(string: str) -> bool:
    char_set = set(string)
    return all([string.count(char) == 1 for char in char_set])


def get_num_chars_processed_before_marker_found(datastream_buffer: str, marker_size: int) -> int:
    for i in range(marker_size - 1, len(datastream_buffer)):
        if are_all_chars_unique(datastream_buffer[i-(marker_size-1):i+1]):
            return i + 1
    return -1


def part1_solution(puzzle_input: str) -> int:
    return get_num_chars_processed_before_marker_found(puzzle_input, 4)


def part2_solution(puzzle_input):
    return get_num_chars_processed_before_marker_found(puzzle_input, 14)


if __name__ == "__main__":
    day6_puzzle_input = load_puzzle_input("./input.txt")
    print(f"(Day 6 Part 1) Characters processed before the first start-of-packet marker detected: {part1_solution(day6_puzzle_input)}")
    print(f"(Day 5 Part 2) Characters processed before the first start-of-message marker detected: {part2_solution(day6_puzzle_input)}")
