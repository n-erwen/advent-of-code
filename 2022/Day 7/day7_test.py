import unittest
import day7

TEST_INPUT = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""


class TestDay7(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(day7.part1_solution(TEST_INPUT), 95437)

    def test_part2(self):
        pass


if __name__ == "__main__":
    unittest.main()
