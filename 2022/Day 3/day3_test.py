import unittest
import day3

SAMPLE_INPUT = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""


class TestDay3(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(day3.part1_solution(
            day3.split_rucksacks(SAMPLE_INPUT)), 157)

    def test_part2(self):
        self.assertEqual(day3.part2_solution(
            day3.split_rucksacks(SAMPLE_INPUT)), 70)


if __name__ == '__main__':
    unittest.main()
