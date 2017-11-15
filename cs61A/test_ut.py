import unittest
import unit_test

class TestUnitTest(unittest.TestCase):

	def test_add(self):
		self.assertEqual(unit_test.add(10,5), 15)
		self.assertEqual(unit_test.add(-1,1), 0)
		self.assertEqual(unit_test.add(-1,-1), -2)

	def test_subtract(self):
		self.assertEqual(unit_test.substract(10,5), 5)
		self.assertEqual(unit_test.substract(-1,1), -2)
		self.assertEqual(unit_test.substract(-1,-1), 0)	

	def test_divide(self):
		# use context manager for exception test
		with self.assertRaises(ValueError):
			unit_test.divide(10, 0)
			
if __name__ == '__main__':
	unittest.main()

