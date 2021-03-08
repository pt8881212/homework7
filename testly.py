

import unittest
import checkLeapYear

class TestCase(unittest.TestCase):
	def test1(self):
		self.assertEqual(checkLeapYear.ly(2020), "Not a Leap year");


if __name__ == '__main__':
	unittest.main();