import unittest
import day5

SAMPLE_INPUT = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""".strip("\n")


class TestDay1(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(day5.part1_solution(SAMPLE_INPUT), "CMZ")

    def test_part2(self):
        pass


if __name__ == "__main__":
    unittest.main()
