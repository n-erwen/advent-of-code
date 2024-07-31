import unittest
import day3

TEST_INPUT = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


class TestDay2(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(day3.part1_solution(TEST_INPUT), 4361)

    # def test_part2(self):
    #     self.assertEqual(day3.part2_solution(TEST_INPUT), 2286)


if __name__ == "__main__":
    unittest.main()
