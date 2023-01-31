import unittest
import binary_gap

class TestBinaryGap(unittest.TestCase):

    
    def test_no_gap(self):

        num = 32 # 100000 has no binary gap

        self.assertEqual(binary_gap.solution(num),(0))

    def test_second_example(self):

        num = 1041 # 10000010001 has longest binary gap 5

        self.assertEqual(binary_gap.solution(num),(5))

    def test_highest_of_two_example(self):

        num = 529 # has two binary gaps, 4 and 3, hence get maximum

        self.assertEqual(binary_gap.solution(num),(4))

    def test_only_ones(self):

        num = 15 # has two binary gaps, 4 and 3, hence get maximum

        self.assertEqual(binary_gap.solution(num),(0))


if __name__ == '__main__':
    unittest.main()
