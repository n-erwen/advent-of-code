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


def get_contiguous_set_of_addends_from_array(num_array, target):
    for index in range(len(num_array)):
        largest_index = 0
        addends_set = []
        sum_of_addends_set = 0

        while sum_of_addends_set < target and largest_index + 1 != len(num_array):
            largest_index += 1
            addends_set = num_array[index:largest_index+1]
            sum_of_addends_set = sum(addends_set)

        if sum_of_addends_set == target:
            return addends_set

    return []


def part1_solution(input, preamble_size):
    return get_first_num_not_sum_of_prev_25_nums(
        transform_all_items_to_integers(input), preamble_size
    )


def part2_solution(input, preamble_size):
    num_array = transform_all_items_to_integers(input)
    invalid_number = get_first_num_not_sum_of_prev_25_nums(
        num_array, preamble_size
    )

    contiguous_addends = get_contiguous_set_of_addends_from_array(num_array, invalid_number)

    return min(contiguous_addends) + max(contiguous_addends)


if __name__ == "__main__":
    puzzle_input = transform_all_items_to_integers(load_input('./input.txt'))
    print('Day 9 Part 1 Answer: ' + str(part1_solution(puzzle_input, 25)))
    print('Day 9 Part 2 Answer: ' + str(part2_solution(puzzle_input, 25)))