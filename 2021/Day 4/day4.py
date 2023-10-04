def load_input(file_path):
    with open(file_path, "r") as f:
        return f.read()


def parse_bingo_board(bingo_board):
    return [
        [{"num": int(num), "marked": False} for num in row.split()]
        for row in bingo_board.split("\n")
    ]


def mark_bingo_boards(bingo_boards, draw_list):
    return [
        [
            [{**cell, "marked": True} if cell["num"] in draw_list else cell for cell in row]
            for row in board
        ]
        for board in bingo_boards
    ]


def does_board_have_complete_row(bingo_board):
    if any([all([cell["marked"] for cell in row]) for row in bingo_board]):
        return True
    return False


def does_board_have_complete_column(bingo_board):
    if any([all([cell["marked"] for cell in row]) for row in list(zip(*bingo_board))]):
        return True
    return False


def does_board_win(bingo_board):
    if does_board_have_complete_row(bingo_board) or does_board_have_complete_column(bingo_board):
        return True
    return False


def calculate_board_final_score(board, last_num_drew):
    return sum([cell["num"] for row in board for cell in row if not cell["marked"]]) * last_num_drew


def calculate_final_score_of_first_board_to_win(bingo_boards, draw_list):
    marked_bingo_boards = mark_bingo_boards(bingo_boards, draw_list[:4])
    for num_drew in draw_list[4:]:
        marked_bingo_boards = mark_bingo_boards(marked_bingo_boards, [num_drew])
        for board in marked_bingo_boards:
            if does_board_win(board):
                return calculate_board_final_score(board, num_drew)


def calculate_final_score_of_last_board_to_win(bingo_boards, draw_list):
    marked_bingo_boards = mark_bingo_boards(bingo_boards, draw_list[:4])

    for num_drew in draw_list[4:]:
        marked_bingo_boards = mark_bingo_boards(marked_bingo_boards, [num_drew])

        if len(marked_bingo_boards) == 1 and does_board_win(marked_bingo_boards[0]):
            return calculate_board_final_score(marked_bingo_boards[0], num_drew)

        for board in marked_bingo_boards:
            if does_board_win(board):
                marked_bingo_boards.remove(board)

    return 0


def part1_solution(bingo_input):
    number_draw, *bingo_boards = bingo_input.split("\n\n")
    parsed_bingo_boards = [parse_bingo_board(board) for board in bingo_boards]
    draw_list = [int(num) for num in number_draw.split(',')]
    return calculate_final_score_of_first_board_to_win(parsed_bingo_boards, draw_list)


def part2_solution(bingo_input):
    number_draw, *bingo_boards = bingo_input.split("\n\n")
    parsed_bingo_boards = [parse_bingo_board(board) for board in bingo_boards]
    draw_list = [int(num) for num in number_draw.split(',')]
    return calculate_final_score_of_last_board_to_win(parsed_bingo_boards, draw_list)


if __name__ == "__main__":
    day4_input = load_input('./input.txt')

    print("(Day 4 Part 1) Final score of bingo board which won first: {}".format(
        part1_solution(bingo_input=day4_input)
    ))

    print("(Day 4 Part 2) Final score of bingo board which won last: {}".format(
        part2_solution(bingo_input=day4_input)
    ))
