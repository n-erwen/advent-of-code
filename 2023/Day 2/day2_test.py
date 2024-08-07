import unittest
import day2

TEST_INPUT = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""



class TestDay2(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(day2.part1_solution(TEST_INPUT), 8)

    def test_part2(self):
        self.assertEqual(day2.part2_solution(TEST_INPUT), 2286)


if __name__ == "__main__":
    unittest.main()
