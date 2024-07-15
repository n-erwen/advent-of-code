def load_input(file_path):
    with open(file_path, "r") as file:
        return file.read().split("\n")


def transform_all_items_to_integers(arr):
    return [int(i) for i in arr]


def get_first_num_not_sum_of_prev_25_nums(num_array, preamble_size):
    for i in range(preamble_size, len(num_array)):
        prev_nums_array = num_array[i - preamble_size:i]
        if not any([
            (num_array[i] - prev_num != num_array[i]
             and num_array[i] - prev_num in prev_nums_array)
            for prev_num in prev_nums_array
        ]):
            return num_array[i]


def part1_solution(input, preamble_size):
    return get_first_num_not_sum_of_prev_25_nums(
        transform_all_items_to_integers(input), preamble_size
    )


if __name__ == "__main__":
    puzzle_input = transform_all_items_to_integers(load_input('./input.txt'))
    print('Day 1 Part 1 Answer: ' + str(part1_solution(puzzle_input, 25)))
