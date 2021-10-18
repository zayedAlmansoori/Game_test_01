#!/usr/bin/env python3
import peeps


def calc_salary(emp):
    salary = emp.salary * 12
    return salary

if __name__ == '__main__':
    z = peeps.Person('zayed')
    k = peeps.Employee('karima', 1700)
    a = 'd'
    print(calc_salary(k))

