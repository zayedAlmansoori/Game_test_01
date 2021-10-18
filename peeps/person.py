#! usr/bin/env python3

class Person:
    def __init__(self, name):
        """
        base person class
        :param name:
        """
        self.name = name



    def __str__(self):
        """
        :return: string
        """
        assert isinstance(self.name, object)
        return f'name: {self.name}'
