import unittest
import golden_fibonacci_nuggets



class TestFibNuggets(unittest.TestCase):

    def test_first_ten(self):

        self.assertEqual(golden_fibonacci_nuggets.find_golden_fib_nugget(1),2)
        self.assertEqual(golden_fibonacci_nuggets.find_golden_fib_nugget(5),4895)
        self.assertEqual(golden_fibonacci_nuggets.find_golden_fib_nugget(10),74049690)

if __name__ == '__main__':
    unittest.main()