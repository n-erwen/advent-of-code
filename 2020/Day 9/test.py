import unittest
from day9 import day9, transform_all_items_to_integers

SAMPLE_INPUT = transform_all_items_to_integers([
    '35', '20', '15', '25', '47', '40', '62', '55', '65', '95',
    '102', '117', '150', '182', '127', '219', '299', '277', '309', '576'
])


class TestDay9(unittest.TestCase):
    def test_sample_input(self):
        self.assertEqual(day9(SAMPLE_INPUT, 5), 127)


if __name__ == '__main__':
    unittest.main()