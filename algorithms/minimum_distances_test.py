import unittest
import minimum_distances

class TestMinimumDistances(unittest.TestCase):

    
    def test_first_example(self):

        arr = [3,2,1,2,3]

        self.assertEqual(minimum_distances.minimum_distance(arr),(2))

    def test_second_example(self):

        arr_two = [7,1,3,4,1,7]

        self.assertEqual(minimum_distances.minimum_distance(arr_two),(3))

    def test_no_pair(self):

        arr_two = [7,1,3,4]

        self.assertEqual(minimum_distances.minimum_distance(arr_two),(-1))

    def test_empty(self):

        arr_two = []

        self.assertEqual(minimum_distances.minimum_distance(arr_two),(-1))


if __name__ == '__main__':
    unittest.main()