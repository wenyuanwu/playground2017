import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

	def setUp(self):
		self.emp_1 = Employee('Corey', 'Schafer', 50000)
		self.emp_2 = Employee('Sue', 'Smith', 60000)

	def tearDown(self):
		pass

	def test_email(self):	
		self.assertEqual(self.emp_1.email(), 'Corey.Schafer@gmail.com')
		self.emp_1.first = "Ernest"
		self.assertEqual(self.emp_1.email(), 'Ernest.Schafer@gmail.com')
		
if __name__ == "__main__":
	unittest.main()	


