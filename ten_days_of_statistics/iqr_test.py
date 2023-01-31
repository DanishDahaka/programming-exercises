import unittest
import interquartile_range

class TestIQR(unittest.TestCase):

    
    def test_first_example(self):

        val = [6,12,8,10,20,16]

        freq = [5,4,3,2,1,5]

        self.assertEqual(interquartile_range.calculate_iqr([i for l in ([a]*f for a, f in zip(val, freq)) for i in l]),(9.0))


    def test_case_five(self):

        val = [10,40,30,50,20]

        freq = [1,2,3,4,5]

        self.assertEqual(interquartile_range.calculate_iqr([i for l in ([a]*f for a, f in zip(val, freq)) for i in l]),(30.0))



if __name__ == '__main__':
    unittest.main()