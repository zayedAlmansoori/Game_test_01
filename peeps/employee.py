import peeps


class Employee(peeps.Person):
    def __init__(self, name, salary):
        """
        Employee
        :param name: employee name
        :param salary: employee salary
        """
        super().__init__(name)
        self.salary = salary

    def __str__(self):
        super().__str__()
        return f'name: {self.name} salary: {self.salary}'
