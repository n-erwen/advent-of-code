import unittest
import day1

SAMPLE_INPUT = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""


class TestDay1(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(day1.part1_solution(day1.split_inventories(SAMPLE_INPUT)), 24000)

    def test_part2(self):
        self.assertEqual(day1.part2_solution(day1.split_inventories(SAMPLE_INPUT)), 45000)


if __name__ == '__main__':
    unittest.main()