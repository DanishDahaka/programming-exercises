import unittest
import chocolate_feast

class TestChoco(unittest.TestCase):

    
    def test_first_example(self):

        self.assertEqual(chocolate_feast.calc_number_chocs(10,2,5),(6))

    def test_second_example(self):

        self.assertEqual(chocolate_feast.calc_number_chocs(12,4,4),(3))

    def test_third_example(self):

        self.assertEqual(chocolate_feast.calc_number_chocs(6,2,2),(5))



if __name__ == '__main__':
    unittest.main()