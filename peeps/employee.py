import peeps
import time
import json
import os


class Employee(peeps.Person):
    def __init__(self, name, salary):
        """
        Employee constructor
        :param name: employee name
        :param salary: employee salary
        """
        super().__init__(name)
        path = self.locate_file()
        if path is not None:
            print("User exists... loading data")
            self.load()
            print(self)
        else:
            self.salary = int(salary)
            self.leave_balance = 30
            self.join_date = time.time()
            self.update()

    def submit_leave(self, days):
        """
        submit leave request
        :param days : number of leave days
        :return:
        """
        if days > 7 or days <= 0:
            raise Exception(f'The number of days is invalid.')
        else:
            self.leave_balance = self.leave_balance - days
            print(f'{self.name} is leaving for {days} days.')
            self.update()

    def load(self):
        """
        loads parameters if file exists
        :return:
        """
        with open(self.name, 'r') as f:
            params = json.load(f)
            self.salary = params['salary']
            self.leave_balance = params['leave_balance']
            self.join_date = params['join_date']

    def update(self):
        """
        writes employee info into json file. Call every time a change is made.
        :return:
        """
        with open(self.name, 'w') as f:
            employee_info = {
                "name": self.name,
                "salary": self.salary,
                "leave_balance": self.leave_balance,
                "join_date": self.join_date
            }
            json_string = json.dumps(employee_info)
            f.write(json_string)

    def __str__(self):
        """
        Returns Employee information when printed
        :return: str
        """
        super().__str__()
        employee_info = f"""
            "name": {self.name},
            "salary": {self.salary},
            "leave_balance": {self.leave_balance},
            "join_date": {self.join_date}"""

        return employee_info

    def locate_file(self):
        """
        returns path if user file exists
        :return: path
        """
        for root, dirs, files in os.walk(os.getcwd()):
            for file in files:
                if file == self.name:
                    path = os.path.join(os.path.dirname(file), file)
                    return path
