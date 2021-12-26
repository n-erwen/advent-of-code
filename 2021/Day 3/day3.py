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
    
def get_oxygen_generator_rating(report):
    filtered_report = report
    for i in range (0, len(report[0])):
        most_common_bit = find_most_common_bit(i, filtered_report)
        filtered_report = [r for r in filtered_report if r[i] == most_common_bit]
        if len(filtered_report) == 1:
            return int(filtered_report[0], base=2)


def get_co2_scrubber_rating(report):
    filtered_report = report
    for i in range (0, len(report[0])):
        least_common_bit = find_least_common_bit(i, filtered_report)
        filtered_report = [r for r in filtered_report if r[i] == least_common_bit]
        if len(filtered_report) == 1:
            return int(filtered_report[0], base=2)
    
INPUT_FILE_PATH = './input.txt'

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
        return get_oxygen_generator_rating(report) * get_co2_scrubber_rating(report)
    print("(Day 3 Part 2) oxygen generator rating * CO2 scrubber rating = {}".format(
        part2()
    ))
