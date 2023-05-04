import unittest
from day1 import part1_solution, part2_solution


class TestDay1(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(part1_solution([12]), 2)
        self.assertEqual(part1_solution([14]), 2)
        self.assertEqual(part1_solution([1969]), 654)
        self.assertEqual(part1_solution([100756]), 33583)

    def test_part2(self):
        self.assertEqual(part2_solution([14]), 2)
        self.assertEqual(part2_solution([1969]), 966)
        self.assertEqual(part2_solution([100756]), 50346)


if __name__ == "__main__":
    unittest.main()
