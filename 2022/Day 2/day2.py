from typing import List

OPPONENT_SHAPES = {"A": "rock", "B": "paper", "C": "scissors"}
PLAYER_SHAPES = {"X": "rock", "Y": "paper", "Z": "scissors"}
DESIRED_OUTCOMES = {"X": "lose", "Y": "draw", "Z": "win"}

SHAPE_NEEDED_TO_WIN = {"rock": "paper",
                       "paper": "scissors", "scissors": "rock"}
SHAPE_NEEDED_TO_LOSE = {"rock": "scissors",
                        "paper": "rock", "scissors": "paper"}

SHAPE_POINTS = {"rock": 1, "paper": 2, "scissors": 3}
OUTCOME_POINTS = {"win": 6, "draw": 3, "lose": 0}


def load_puzzle_input(file_name: str) -> str:
    with open(file_name, "r") as file:
        return file.read().rstrip()


def split_rounds(input_string: str) -> List[str]:
    return [r for r in input_string.split("\n")]


def get_round_outcome(player, opponent):
    if player == opponent:
        return "draw"
    if player == SHAPE_NEEDED_TO_WIN[opponent]:
        return "win"
    if player == SHAPE_NEEDED_TO_LOSE[opponent]:
        return "lose"


def get_required_response_for_outcome(outcome: str, opponent: str):
    if outcome == "draw":
        return opponent

    if outcome == "win":
        return SHAPE_NEEDED_TO_WIN[opponent]

    if outcome == "lose":
        return SHAPE_NEEDED_TO_LOSE[opponent]


def decode_columns(game_round, second_column: {str: str}):
    return [
        OPPONENT_SHAPES[code]
        if code in ("A", "B", "C")
        else second_column[code]
        for code in game_round.split(" ")
    ]


def first_strategy_get_round_score(game_round: str) -> int:
    opponent_shape, player_shape = decode_columns(
        game_round, second_column=PLAYER_SHAPES)

    return SHAPE_POINTS[player_shape] \
        + OUTCOME_POINTS[get_round_outcome(player_shape, opponent_shape)]


def second_strategy_get_round_score(game_round: str):
    opponent_shape, desired_outcome = decode_columns(
        game_round, second_column=DESIRED_OUTCOMES)

    return SHAPE_POINTS[get_required_response_for_outcome(desired_outcome, opponent_shape)] \
        + OUTCOME_POINTS[desired_outcome]


def part1_solution(game_rounds: List[str]) -> int:
    """Part 1: Total score of Rock Paper Scissors rounds when second column is player response"""
    return sum([first_strategy_get_round_score(r) for r in game_rounds])


def part2_solution(game_rounds: List[str]) -> int:
    """Part 2: Total score of rounds when second column is desired outcome"""
    return sum([second_strategy_get_round_score(r) for r in game_rounds])


if __name__ == "__main__":
    rounds_input = split_rounds(load_puzzle_input("./input.txt"))
    print(f"Part 1 Solution: {part1_solution(rounds_input)}")
    print(f"Part 2 Solution: {part2_solution(rounds_input)}")
