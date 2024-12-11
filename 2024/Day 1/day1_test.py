import unittest
import day2

TEST_INPUT = """\
3   4
4   3
2   5
1   3
3   9
3   3"""


class TestDay2(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(day2.part1_solution(TEST_INPUT), 11)

    def test_part2(self):
        self.assertEqual(day2.part2_solution(TEST_INPUT), 31)


if __name__ == "__main__":
    unittest.main()
