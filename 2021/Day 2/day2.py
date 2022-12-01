from typing import List


def load_puzzle_input(file_name):
    with open(file_name, "r") as f:
        return f.read().rstrip()


def split_commands(input_string: str) -> List[str]:
    return input_string.split("\n")


def total_distance_travelled_in_direction(direction, cmds, end=-1):
    end = len(cmds) if end == -1 else end
    return sum([
        int(cmds[i].split(" ")[1]) for i in range(0,end) 
        if cmds[i].split(" ")[0] == direction
    ])


def get_final_horizontal_position(cmds):
    return total_distance_travelled_in_direction("forward", cmds)


def get_final_depth(cmds):
    return total_distance_travelled_in_direction("down", cmds) - total_distance_travelled_in_direction("up", cmds)


def get_final_aimed_depth(cmds):
    return sum([
        int(cmds[i].split(" ")[1]) * (
            total_distance_travelled_in_direction("down", cmds, end=i) - total_distance_travelled_in_direction("up", cmds, end=i)
        ) for i in range(0, len(cmds)) 
        if cmds[i].split(" ")[0] == "forward"
    ])


def part1_solution(commands: List[str]) -> int:
    """Part 1: Product of submarine's final horizontal position and final depth"""
    return get_final_depth(commands) * get_final_horizontal_position(commands)


def part2_solution(commands: List[str]) -> int:
    """Part 2: Product of submarine's final horizontal position and final depth,
    when final depth has been multiplied with aim"""
    return get_final_aimed_depth(commands) * get_final_horizontal_position(commands)


if __name__ == "__main__":
    commands_input = split_commands(load_puzzle_input("./input.txt"))
    print(f"Part 1 Solution: {part1_solution(commands_input)}")
    print(f"Part 2 Solution: {part2_solution(commands_input)}")

