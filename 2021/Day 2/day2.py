def load_input(file_path):
    with open(file_path, "r") as f:
        return f.read().split("\n")

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

INPUT_FILE_PATH = './input.txt'

if __name__ == "__main__":
    commands = load_input(INPUT_FILE_PATH)
    # PART 1
    def part1():
        return get_final_depth(commands) * get_final_horizontal_position(commands)
    print("(Day 2 Part 1) Final horizontal position * final depth = {}".format(
        part1()
    ))
    
    # PART 2
    def part2():
        return get_final_aimed_depth(commands) * get_final_horizontal_position(commands)
    print("(Day 2 Part 2) Final horizontal position * final depth = {}".format(
        part2()
    ))
