import unittest
import no_6_sum_square_difference

class TestViralAdvertising(unittest.TestCase):

    def test_first_example(self):

        self.assertEqual(no_6_sum_square_difference.calculate(3),(22))

    
    def test_another_example(self):

        self.assertEqual(no_6_sum_square_difference.calculate(10),(2640))



if __name__ == '__main__':
    unittest.main()