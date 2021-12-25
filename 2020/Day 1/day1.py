def load_input(file_path):
    with open(file_path, "r") as f:
        return [int(x) for x in f.read().split("\n")]
    
def find_product_of_two_nums_which_sum_to(target_sum, num_array):
    """Day 1 Part 1: Find the product of two numbers which sum to 2020"""
    for x in num_array:
        for y in num_array:
            if (x + y) == target_sum:
                return x * y

def find_product_of_three_nums_which_sum_to(target_sum, num_array):
    """Day 1 Part 2: Find the product of three numbers which sum to 2020"""
    for x in num_array:
        for y in num_array:
            for z in num_array:
                if (x + y + z) == target_sum:
                    return x * y * z

if __name__ == "__main__":
    expenses = load_input("./input.txt")
    print("(Day 1: Part 1) Result: " + str(find_product_of_two_nums_which_sum_to(2020, expenses)))
    print("(Day 1: Part 2) Result: " + str(find_product_of_three_nums_which_sum_to(2020, expenses)))
