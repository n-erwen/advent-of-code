def load_puzzle_input(file_name: str) -> str:
    with open(file_name, "r") as file:
        return file.read().rstrip()


CUBE_BAG = {"red": 12, "green": 13, "blue": 14}


def parse_set_data(set_data: str):
    """Returns a dictionary with cube color and amounts from string of set data.
    :param set_data: string containing set data (e.g. "3 blue, 4 red")
    :returns: dictionary with cube colors and respective amounts
        (e.g. {"blue": 3, "red": 4})
    """

    return {
        cube.split(" ")[1]: int(cube.split(" ")[0])
        for cube in set_data.split(", ")
    }


def parse_game_data(game_data: str):
    [game_id, game_data] = game_data.split(": ")
    return {
        "id": int(game_id.replace("Game ", "")),
        "sets": [parse_set_data(game_set) for game_set in game_data.split("; ")]
    }


def part1_solution(puzzle_input: str) -> int:
    parsed_game_data = [parse_game_data(game_data)
                        for game_data in puzzle_input.split("\n")]
    return sum([game['id'] for game in parsed_game_data if all([
        all([
            game_set[cube_color] <= CUBE_BAG[cube_color]
            for cube_color in game_set.keys()
        ])
        for game_set in game['sets']
    ])])


def part2_solution(puzzle_input: str) -> int:
    parsed_game_data = [parse_game_data(game_data)
                        for game_data in puzzle_input.split("\n")]
    # for each game
    # find the largest amount for each ball color across the sets
    # multiply 
    return -1


if __name__ == "__main__":
    day2_puzzle_input = load_puzzle_input("./input.txt")
    print(f"(Day 2 Part 1) Solution: {part1_solution(day2_puzzle_input)}")
    print(f"(Day 2 Part 2) Solution: {part2_solution(day2_puzzle_input)}")
