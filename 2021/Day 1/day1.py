from typing import List


def load_puzzle_input(file_name: str) -> str:
    with open(file_name, "r") as file:
        return file.read().rstrip()


def split_sonar_sweep_measurements(input_string: str) -> List[int]:
    return [int(s) for s in input_string.split("\n")]


def num_times_measurements_increased(m):
    return len([i for i in range(1, len(m)) if m[i] > m[i-1]])


def get_three_measurement_windows(m):
    return [sum([m[i] for i in range(n, n+3)]) for n in range(0, len(m)) if n+2 < len(m)]


def part1_solution(sonar_sweep_measurements: List[int]):
    """Part 1: Number of times a sonar depth measurement increases from the previous measurement"""
    return num_times_measurements_increased(
        sonar_sweep_measurements
    )


def part2_solution(sonar_sweep_measurements: List[int]):
    """Part 2: Number of times the sum of measurements from a three-measurement sliding window increases from the
    previous sum"""
    return num_times_measurements_increased(get_three_measurement_windows(sonar_sweep_measurements))


if __name__ == "__main__":
    measurements_input = split_sonar_sweep_measurements(load_puzzle_input("./input.txt"))
    print(f"Part 1 Solution: {part1_solution(measurements_input)}")
    print(f"Part 2 Solution: {part2_solution(measurements_input)}")
