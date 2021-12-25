def load_input(file_path):
    with open(file_path, "r") as f:
        return f.read().split("\n")

def is_second_measurement_larger(m1, m2):
    return m2 > m1

def num_times_measurements_increased(m):
    return len([
        i for i in range(1, len(m)) 
        if m[i] > m[i-1]
    ])

def get_three_measurement_windows(m):
    return [
        sum([m[i] for i in range(n, n+3)]) 
        for n in range(0,len(m)) 
        if n+2 < len(m)
    ]

INPUT_FILE_PATH = './input.txt'
    
if __name__ == "__main__":
    sonar_sweep_measurements = [int(s) for s in load_input(INPUT_FILE_PATH)]
    # PART 1
    def part1():
        return num_times_measurements_increased(
            sonar_sweep_measurements
        )
    print("(Day 1 Part 1) Number of measurements larger than the previous measurement: {}".format(
        part1()
    ))
    
    # PART 2
    def part2():
        return num_times_measurements_increased(
            get_three_measurement_windows(sonar_sweep_measurements)
        )
    print("(Day 1 Part 2) Number of measurements larger than the previous measurement: {}".format(
        part2()
    ))