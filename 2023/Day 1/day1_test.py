import unittest
import day1


class TestDay1(unittest.TestCase):
    def test_part1(self):
        test_input = """1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet"""
        self.assertEqual(day1.part1_solution(test_input), 142)

    def test_part2(self):
        test_input = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
        self.assertEqual(day1.part2_solution(test_input), 281)


if __name__ == "__main__":
    unittest.main()
