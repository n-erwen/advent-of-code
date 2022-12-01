import unittest
import day2

SAMPLE_INPUT = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

PUZZLE_INPUT = day2.load_puzzle_input("./input.txt")


class TestDay1(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(day2.part1_solution(day2.split_commands(SAMPLE_INPUT)), 150)

    def test_part2(self):
        self.assertEqual(day2.part2_solution(day2.split_commands(SAMPLE_INPUT)), 900)


if __name__ == '__main__':
    unittest.main()
