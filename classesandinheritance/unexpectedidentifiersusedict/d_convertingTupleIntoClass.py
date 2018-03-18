"""
    This module demonstrates how you can reduce complexity by removing
    layers of dictionary df dictionaries (or tuples).

    Tuples in general are positional. If you want to associate more
    information with a tuple you have to rewrite the whole tuple.
        - As soon as you find yourself going longer than a two-tupele
          it's time to consider a different approach.

    The 'namedtuple' type lets you define tiny, immutable data classes.
        - The fields are accessible with named attributes, making it
          easy to move to your won class
        - If you need to add behaviors to the simple data containers.

    The refactoring happens in these steps
        1. Start at the bottom of the dependency tree: as sling grade.
           Move grade to a 'namedtuple'

           Grade = collections.namedtuple('Grade', ('scope', 'weight'))

        2. Write a class to represent a single subject that contains a
           set of grades.

        3. Write a class to represent a set of subjects that are being
           studied by a single student

        4. Write a container for all of the studets keyed dynamically
           by their names
"""

import collections


Grade = collections.namedtuple('Grade', ('score', 'weight'))


class Subject(object):
    """
        2. Write a class to represent a single subject that contains a
           set of grades.
    """
    def __init__(self):
        self.__grades = []

    def report_grade(self, score, weight):
        self.__grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self.__grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight


class Student(object):
    """
        3. Write a class to represent a set of subjects that are being
           studied by a single student
    """
    def __init__(self):
        self.__subjects = {}

    def subject(self, name):
        self.__subjects.setdefault(name, Subject())
        return self.__subjects[name]

    def average_grade(self):
        total, count = 0, 0
        for subject in self.__subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count


class Gradebook(object):
    """
        4. Write a container for all of the studets keyed dynamically
           by their names
    """
    def __init__(self):
        self.__students = {}

    def student(self, name):
        self.__students.setdefault(name, Student())
        return self.__students[name]


book = Gradebook()
albert = book.student('Albert Einstein')
math = albert.subject('Math')
math.report_grade(85, .10)
math.report_grade(100, .5)
math.report_grade(100, .9)
print(albert.average_grade())