"""This is Module 2"""


class Person:
    def __init__(self, name):
        self.name = name 

    def __str__(self):
        return f"{self.name}"
