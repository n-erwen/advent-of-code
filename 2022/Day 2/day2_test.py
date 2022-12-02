import unittest
import day2

SAMPLE_INPUT = """A Y
B X
C Z"""


class TestDay1(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(day2.part1_solution(day2.split_rounds(SAMPLE_INPUT)), 15)

    def test_part2(self):
        self.assertEqual(day2.part2_solution(day2.split_rounds(SAMPLE_INPUT)), 12)


if __name__ == '__main__':
    unittest.main()
