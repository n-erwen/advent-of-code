def move_down_slope(x,y,pattern_len):
    x += 3
    if x > pattern_len - 1:
        x -= pattern_len
    y += 1
    return [x,y]

def is_square_open_or_tree(pos):
    if pos == "#":
        return "X"
    elif pos == ".":
        return "O"

if __name__ == "__main__":
    input_file = open("input.txt", "r")
    toboggan_map = input_file.read().split("\n")
    input_file.close()
    map_pattern_length = len(toboggan_map[0])
    x = 0
    y = 0

    while y < len(toboggan_map)-1:
        x,y = move_down_slope(x,y,map_pattern_length)
        toboggan_map[y] = toboggan_map[y][:x] + is_square_open_or_tree(toboggan_map[y][x]) + toboggan_map[y][x:]

    print("Part 1: " + str("\n".join(toboggan_map).count("X")))
