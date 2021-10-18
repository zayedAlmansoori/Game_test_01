import unittest
import main
import peeps

class TestMain(unittest.TestCase):
    def test_print_person(self):
        employee = peeps.Employee('test', 1700)
        salary = main.calc_salary(employee)
        self.assertEqual(salary, 20400)