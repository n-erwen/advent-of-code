import unittest
import day3

TEST_PART1_INPUT = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
TEST_PART2_INPUT = "@xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

class TestDay3(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(day3.part1_solution(TEST_PART1_INPUT), 161)

    def test_part2(self):
        self.assertEqual(
            day3.part2_solution(TEST_PART2_INPUT), 48)


if __name__ == "__main__":
    unittest.main()
