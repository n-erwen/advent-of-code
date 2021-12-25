def load_input(file_path):
    with open(file_path, "r") as f:
        return f.read().split("\n")

def total_distance_travelled_in_direction(direction, cmds):
    return sum([
        int(c.split(" ")[1]) for c in cmds 
        if c.split(" ")[0] == direction
    ])

def get_final_horizontal_position(cmds):
    return total_distance_travelled_in_direction("forward", cmds)

def get_final_depth(cmds):
    return total_distance_travelled_in_direction("down", cmds) - total_distance_travelled_in_direction("up", cmds)

def get_final_aimed_depth(cmds):
    final_depth = 0
    for c in cmds:
        direction, amount = c.split(" ")[0], int(c.split(" ")[1])
        if direction == "up":
            final_depth += amount
        elif direction == "down":
            final_depth -= amount
        elif direction == "forward":
            final_depth += amount*final_depth
    return final_depth

IS_EXAMPLE = True
INPUT_FILE_PATH = './example_input.txt' if IS_EXAMPLE else './input.txt'

if __name__ == "__main__":
    commands = load_input(INPUT_FILE_PATH)
    # PART 1
    def part1():
        return get_final_depth(commands) * get_final_horizontal_position(commands)
    part1_result = part1()
    print("(Day 2 Part 1) Final horizontal position * final depth = {}".format(part1_result))
    if IS_EXAMPLE:
        assert part1_result == 150, "Expected 150, received {}".format(part1_result)
    
    # PART 2
    def part2():
        return get_final_aimed_depth(commands) * get_final_horizontal_position(commands)
    part2_result = part2()
    print("(Day 2 Part 2) Final horizontal position * final depth = {}".format(part2_result))
    if IS_EXAMPLE:
        assert part2_result == 900, "Expected 900, received {}".format(part2_result)
