import unittest
import day6


class TestDay1(unittest.TestCase):
    def test_part1(self):
        test_cases = [
            {"input": "mjqjpqmgbljsphdztnvjfqwrcgsmlb", "expected": 7},
            {"input": "bvwbjplbgvbhsrlpgdmjqwftvncz", "expected": 5},
            {"input": "nppdvjthqldpwncqszvftbrmjlhg", "expected": 6},
            {"input": "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", "expected": 10},
            {"input": "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", "expected": 11}
        ]

        for case in test_cases:
            self.assertEqual(
                day6.part1_solution(case["input"]), case["expected"],
                msg="part1_solution(\"{}\") != {}".format(case["input"], case["expected"])
            )

    def test_part2(self):
        test_cases = [
            {"input": "mjqjpqmgbljsphdztnvjfqwrcgsmlb", "expected": 19},
            {"input": "bvwbjplbgvbhsrlpgdmjqwftvncz", "expected": 23},
            {"input": "nppdvjthqldpwncqszvftbrmjlhg", "expected": 23},
            {"input": "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", "expected": 29},
            {"input": "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", "expected": 26}
        ]

        for case in test_cases:
            self.assertEqual(
                day6.part2_solution(case["input"]), case["expected"],
                msg="part2_solution(\"{}\") != {}".format(case["input"], case["expected"])
            )


if __name__ == "__main__":
    unittest.main()
