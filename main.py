#!/usr/bin/env python3
import peeps


def calc_salary(emp):
    """
    calculates annual salary
    :param emp: Employee class
    :return: int
    """
    if not type(emp) == peeps.Employee:
        raise Exception('input is not an instance of Employee.')
    else:
        salary = emp.salary * 12
        return salary

def give_raise(emp, amount):
    """
    raises an employee's salary by the given amount.
    :param emp: Employee instance
    :param amount: raise amount
    :return: None
    """
    if not type(emp) == peeps.Employee:
        raise Exception('input is not an instance of Employee.')
    else:
        emp.salary = emp.salary + int(amount)
        print(f'{emp.name} received a {amount} raise.')
        emp.update()
        print(emp)




if __name__ == '__main__':
    k = peeps.Employee('karima', 1700)
    try:
        pass
    except Exception as e:
        print(f'[!]Error... {e}')

