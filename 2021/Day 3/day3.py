def load_input(file_path):
    with open(file_path, "r") as f:
        return f.read().split("\n")


def get_bit_occurence(bit, pos, report):
    return len([num[pos] for num in report if num[pos] == bit])

def find_most_common_bit(pos, report):
    return "0" if get_bit_occurence("0", pos, report) > get_bit_occurence("1", pos, report) else "1"

def find_least_common_bit(pos, report):
    return "0" if get_bit_occurence("0", pos, report) <= get_bit_occurence("1", pos, report) else "1"

def get_gamma_rate(report):
    return int(
        "".join([find_most_common_bit(i, report)
                 for i in range(0, len(report[0]))
                ]),
        base=2)

def get_epsilon_rate(report):
    return int(
        "".join([find_least_common_bit(i, report)
                 for i in range(0, len(report[0]))
                ]),
        base=2)
    
IS_EXAMPLE = True
INPUT_FILE_PATH = './example_input.txt' if IS_EXAMPLE else './input.txt'

if __name__ == "__main__":
    report = load_input(INPUT_FILE_PATH)
    # PART 1
    def part1():
        return get_gamma_rate(report) * get_epsilon_rate(report)
    print("(Day 3 Part 1) gamma rate * epsilon rate = {}".format(
        part1()
    ))

    # PART 2
    def part2():
        return None
    print("(Day 3 Part 2) {}".format(
        part2()
    ))
    