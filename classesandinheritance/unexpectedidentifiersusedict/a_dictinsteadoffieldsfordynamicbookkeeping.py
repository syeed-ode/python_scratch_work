"""
    This class demonstrates that use of a dictionary instead of fields
    is preferred when the situation requires "dynamic" bookkeeping.

    'Dynamic' means an unexpected set of identifiers.

    #
    # for an unexpected amount of identifiers ('dynamic' bookkeeping) -- utilize
    # dictionary instead of fields.
    #
    # Avoid more than one layer of nesting.
    # break out the inner dictionary into classes.
    #
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
