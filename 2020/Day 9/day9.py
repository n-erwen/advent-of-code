def is_sum_of_two_nums_in_array(num, arr):
    for possible_factor in arr:
        if num - possible_factor in arr:
            return True
    return False


def day9(data, preamble_size):
    for n in range(5, len(data)):
        prev_numbers = data[n-preamble_size:n]
        if data[n] == 20:
            pass
        if not is_sum_of_two_nums_in_array(data[n], prev_numbers):
            return data[n]
    return 0


def load_input(file_path):
    with open(file_path, "r") as file:
        return file.read().split("\n")

def transform_all_items_to_integers(arr):
    return [int(i) for i in arr]

if __name__ == "__main__":
    puzzle_input = transform_all_items_to_integers(load_input('./input.txt'))
    print(day9(puzzle_input, 25))