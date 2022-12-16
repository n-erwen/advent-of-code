import unittest
import day4

SAMPLE_INPUT = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


class TestDay1(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(day4.part1_solution(
            day4.split_input_rows(SAMPLE_INPUT)), 2)

    def test_part2(self):
        self.assertEqual(day4.part2_solution(
            day4.split_input_rows(SAMPLE_INPUT)), 4)


if __name__ == "__main__":
    unittest.main()
