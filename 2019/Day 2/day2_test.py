import unittest
import day2

class TestDay2(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(day2.run_intcode_program([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])[0], 3500)
        self.assertEqual(day2.run_intcode_program([1, 0, 0, 0, 99])[0], 2)
        self.assertEqual(day2.run_intcode_program([1, 1, 1, 4, 99, 5, 6, 0, 99])[0], 30)

    def test_part2(self):
        pass


if __name__ == "__main__":
    unittest.main()
