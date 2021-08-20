import unittest
import day_of_the_programmer

class TestCalendar(unittest.TestCase):

    
    def test_first_example(self):

        year = '2017'

        self.assertEqual(day_of_the_programmer.calculate_day(year),('13.09.2017'))

    def test_second_example(self):

        year_two = '1800'

        self.assertEqual(day_of_the_programmer.calculate_day(year_two),('12.09.1800'))

    def test_1918(self):

        year_three = '1918'

        self.assertEqual(day_of_the_programmer.calculate_day(year_three),('31.08.1918'))



if __name__ == '__main__':
    unittest.main()