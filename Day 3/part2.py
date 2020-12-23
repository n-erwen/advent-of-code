def move_down_slope(slope, pos, pattern_len):
    pos["x"] += slope["right"]
    if pos["x"] > pattern_len - 1:
        pos["x"] -= pattern_len
    pos["y"] += slope["down"]
    return {"x": pos["x"], "y": pos["y"]}

def is_square_open_or_tree(pos):
    if pos == "#":
        return "X"
    elif pos == ".":
        return "O"

def num_of_trees_on_slope(slope, t_map, pattern_len):
    pos = {"x": 0, "y": 0}
    while pos["y"] < len(t_map)-1:
        pos = move_down_slope(slope, pos, pattern_len)
        if pos["y"] > len(t_map) - 1:
            break
        t_map[pos["y"]] = t_map[pos["y"]][:pos["x"]] + is_square_open_or_tree(t_map[pos["y"]][pos["x"]]) + t_map[pos["y"]][pos["x"]:]

    return "\n".join(t_map).count("X")

if __name__ == "__main__":
    input_file = open("input.txt", "r")
    toboggan_map = input_file.read().split("\n")
    input_file.close()
    map_pattern_length = len(toboggan_map[0])

    slopes = [
        {"right": 1, "down": 1},
        {"right": 3, "down": 1},
        {"right": 5, "down": 1},
        {"right": 7, "down": 1},
        {"right": 1, "down": 2},
    ]

    trees_on_each_slope = []
    for s in slopes:
        trees_on_each_slope.append(num_of_trees_on_slope(s, toboggan_map[:], map_pattern_length))

    product = 1
    for trees in trees_on_each_slope:
        product *= trees

    print("Part 2: " + str(product))
