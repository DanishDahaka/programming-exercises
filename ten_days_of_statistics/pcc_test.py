import unittest
import covariance_and_correlation

class TestCovarianceCorrelation(unittest.TestCase):

    
    def test_first_example(self):

        arrx = [10, 9.8, 8, 7.8, 7.7, 7, 6, 5, 4, 2]
        arry = [200, 44, 32, 24, 22, 17, 15, 12, 8, 4]

        self.assertEqual(covariance_and_correlation.calculate_pcc(arrx, arry),(0.612))



if __name__ == '__main__':
    unittest.main()