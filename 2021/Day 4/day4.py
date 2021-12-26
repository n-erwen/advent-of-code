# Our search for the sleigh keys is going peachy so far(!)
def load_input(file_path):
    with open(file_path, "r") as f:
        return f.read().split("\n")
    
def parse_bingo_boards_old(boards_string):
    boards = []
    for b in boards_string.split("\n\n"):
        rows = []
        for r in [row.split(" ") for row in b.split("\n")]:
            rows.append([int(n) for n in r if n != ""])
        boards.append(rows)
    return boards

def parse_bingo_boards(boards_string):
        return [
            int(n) for n in r if n != ""
            for r in row.split(" ")
            for row in b.split("\n")
            for b in boards_string.split("\n\n")
        ]


IS_EXAMPLE = True
INPUT_FILE_PATH = './example_input.txt' if IS_EXAMPLE else './input.txt'

if __name__ == "__main__":
    bingo_input = load_input(INPUT_FILE_PATH)
    number_draw = bingo_input[0]
    bingo_boards = parse_bingo_boards("\n".join(bingo_input[2:]))
    print(bingo_boards)
    # PART 1
    def part1():
        return None
    print("(Day 4 Part 1) Final score of bingo board which won first: {}".format(
        part1()
    ))
    
    # PART 2
    def part2():
        return None
    print("(Day 4 Part 2) {}".format(
        part2()
    ))
