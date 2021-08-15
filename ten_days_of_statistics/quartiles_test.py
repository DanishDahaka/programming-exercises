import unittest
import quartiles

class TestQuartiles(unittest.TestCase):

    
    def test_first_example(self):

        arr = [9,5,7,1,3]

        self.assertEqual(quartiles.quartile_calculations(arr),(2,5,8))

    def test_second_example(self):

        arr_two = [3,7,8,5,12,14,21,15,18,14]

        self.assertEqual(quartiles.quartile_calculations(arr_two),(7,13,15))


if __name__ == '__main__':
    unittest.main()