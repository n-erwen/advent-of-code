from math import floor
from typing import Callable


def read_input_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        return file.read().rstrip()


def read_module_masses(file_name: str) -> list[int]:
    return [int(mass) for mass in read_input_file(file_name).split("\n")]


def calc_fuel_requirement(mass):
    return floor(mass / 3) - 2


def calc_fuel_requirement_with_additional_fuel(mass):
    required_fuel = calc_fuel_requirement(mass)
    if required_fuel > 0:
        return required_fuel + calc_fuel_requirement_with_additional_fuel(required_fuel)
    return 0


def total_fuel_requirement(calculation_func: Callable, masses: list[int]):
    return sum([calculation_func(m) for m in masses])


def part1_solution(masses: list[int]):
    return total_fuel_requirement(calc_fuel_requirement, masses)


def part2_solution(masses: list[int]):
    return total_fuel_requirement(calc_fuel_requirement_with_additional_fuel, masses)


if __name__ == "__main__":
    module_masses = read_module_masses("input.txt")
    print("Part 1 Solution: {}\nPart 2 Solution: {}".format(
        part1_solution(module_masses),
        part2_solution(module_masses)
    ))
