import unittest
import day1

SAMPLE_INPUT = """199
200
208
210
200
207
240
269
260
263"""


class TestDay1(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(day1.part1_solution(day1.split_sonar_sweep_measurements(SAMPLE_INPUT)), 7)

    def test_part2(self):
        self.assertEqual(day1.part2_solution(day1.split_sonar_sweep_measurements(SAMPLE_INPUT)), 5)


if __name__ == '__main__':
    unittest.main()
