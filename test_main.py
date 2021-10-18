import unittest
import main
import peeps

class TestMain(unittest.TestCase):
    def test_print_person(self):
        employee = peeps.Employee('test', 1700)
        salary = main.calc_salary(employee)
        self.assertEqual(salary, 20400)
    def test_give_raise(self):
        emp = peeps.Employee('test2', 1500)
        main.give_raise(emp, 500)
        self.assertEqual(emp.salary, 2000)

if __name__ == "__main__":
    unittest.main()