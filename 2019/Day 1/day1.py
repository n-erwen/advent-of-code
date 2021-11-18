from math import floor

class Part1:
    @staticmethod
    def read_input(filename):
        with open(filename, "r") as f:
            return f.read().split("\n")
        
    @classmethod
    def calc_fuel_requirement(cls, mass):
        return floor(mass/3) - 2
    
    @classmethod
    def total_fuel_requirement(cls, input_file_name):
        module_masses = [int(n) for n in read_input(input_file_name)]
        return sum([cls.calc_fuel_requirement(m) for m in module_masses])
    
    
class Part2(Part1):
    @classmethod
    def calc_fuel_requirement(cls, mass):
        fuel = floor(mass/3) - 2
        if fuel > 0:
            return fuel + calc_fuel_requirement(fuel)
        return 0

if __name__ == "__main__":
    print("Part 1: {}\nPart 2: {}".format(
        Part1.total_fuel_requirement("input.txt"),
        Part2.total_fuel_requirement("input.txt")
    ))
