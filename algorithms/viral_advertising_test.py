import unittest
import viral_advertising

class TestViralAdvertising(unittest.TestCase):

    def test_first_example(self):

        self.assertEqual(viral_advertising.advertise(3),(9))

    
    def test_another_example(self):

        self.assertEqual(viral_advertising.advertise(5),(24))



if __name__ == '__main__':
    unittest.main()