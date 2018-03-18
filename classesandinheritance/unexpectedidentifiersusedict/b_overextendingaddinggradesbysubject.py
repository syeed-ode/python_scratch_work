"""
    This class demonstrates how over utilization of dictionaries
    can be problematic. It is an extension (conceptually, not by
    inheritance) of the dictinsteadoffields module's SimpleGradebook.

    The rule of thumb: NO MORE THAN ONE LEVEL OF NESTING (i.e.
    avoid dictionaries that contain dictionaries).

    #
    # for an unexpected amount of identifiers ('dynamic' bookkeeping) -- utilize
    # dictionary instead of fields.
    #
    # Avoid more than one layer of nesting.
    # break out the inner dictionary into classes.
    #
"""


class BySubjectGradebook(object):
    def __init__(self):
        self.__grades = {}

    def add_student(self, name):
        self.__grades[name] = {}

    # Note the increase in complexity to deal with the multilevel
    # dictionary. Yet this is still considered manageable.

    def report_grade(self, name, subject, grade) -> None:
        """
            This method changes the __grades field (in SimpleGradebook)
            from a dictionary of names (the keys) to grades (the values)
            to a dictionary of a dictionary.

            __grades is now name (the keys) to dictionary [subject (the
            keys) to grades (the values). Note the use of setdefault.

            This method takes advantage of the pass by reference nature of
            lists, dictionaries (and although not used here, sets).
            by_subject gets populated with the updates to grade_list, and
            __grades gets updated when by_subject gets populated.


            :param name:
            :param subject:
            :param grade: a dictionary of dictionaries. name -> dictionary
                   where, dictionary: subject -> grades
            :return:
        """
        by_subject = self.__grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append(grade)
        print("This is grade_list:")
        print(grade_list,end='\n\n')
        print("This is by_subject:")
        print(by_subject,end='\n\n')
        print("This is self.__grades:")
        print(self.__grades,end='\n\n')

    def average_grade(self, name) -> int:
        """
            This method increases in complexity compared to the average_grade
            in SimpleGradebook.

            :param name:
            :return:
        """
        by_subject = self.__grades[name]
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)

        return total / count

book = BySubjectGradebook()
book.add_student('Albert Einstein')
book.report_grade('Albert Einstein', 'Math', 75)
book.report_grade('Albert Einstein', 'Math', 65)
book.report_grade('Albert Einstein', 'Gym', 90)
book.report_grade('Albert Einstein', 'Gym', 95)
print("Albert Einstein's average grade is: %d" % book.average_grade('Albert Einstein'))
