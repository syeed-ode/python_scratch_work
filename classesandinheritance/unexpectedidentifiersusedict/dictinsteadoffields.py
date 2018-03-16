"""
    This class demonstrates that use of a dictionary instead of fields
    are better when the situation requires "dynamic" bookkeeping.

    'Dynamic' means an unexpected set of identifiers.
"""


class SimpleGradebook(object):
    def __init__(self):
        self.__grades = {}

    def add_student(self, name):
        self.__grades[name] = []

    def report_grade(self, name, score):
        self.__grades[name].append(score)

    def average_grade(self, name):
        grades = self.__grades[name]
        return sum(grades) / len(grades)

book = SimpleGradebook()
book.add_student('Issac Newton')
book.report_grade('Issac Newton', 90)
print(book.average_grade('Issac Newton'))
