import unittest
import sequence_equation

class TestSequenceEquation(unittest.TestCase):

    def test_first_example(self):

        self.assertEqual(sequence_equation.permutation_equation([5,2,1,3,4]),([4,2,5,1,3]))

    
    def test_another_example(self):

        self.assertEqual(sequence_equation.permutation_equation([2,3,1]),([2,3,1]))



if __name__ == '__main__':
    unittest.main()