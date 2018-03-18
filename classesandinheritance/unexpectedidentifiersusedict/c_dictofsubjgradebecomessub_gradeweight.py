"""
    This class builds off of overextendingaddinggradesbysubject
    module's BySubjectGradebook. In BySubjectGradebook a dictionary
    consisting of name to another dictionary is use. The inner dictionary
    is a subject (the key) to grade (the value).

    This class now needlessly converts the grade value to a tuple
    consisting of (grade, weight).

    This class demonstrates how nesting dicitionaries/tuples too deeply
    can increase complexity.

    #
    # for an unexpected amount of identifiers ('dynamic' bookkeeping) -- utilize
    # dictionary instead of fields.
    #
    # Avoid more than one layer of nesting.
    # break out the inner dictionary into classes.
    #

"""


class WeightedGradebook(object):
    def __init__(self):
        self.__grades = {}

    def add_student(self, name):
        self.__grades[name] = {}

    def report_grade(self, name, subject, score, weight) -> None:
        """
            Replaced the inner dictionary with a tuple of (grade, weight)
            instead of just utilizing grade.

            Python's built-in dictionaries and tuple types make it easy to
            keep going, adding layer after layer.

            :param name:
            :param subject:
            :param score:
            :param weight:
            :return:
        """
        by_subject = self.__grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append((score, weight))

    def average_grade(self, name) -> 'FloatingPoint':
        """
            This method should avoid a dictionary containing a tuple. It
            is too many levels deep and makes the code brittle.

            It should be broken out into classes. This lets you provide
            well defined interfaces that better encapsulate your data.

            Calculating the total grade by computing the weight score is
            managed by a tuple.

            Refactoring should start at the bottom level. So, converting
            the grade tuple into a class would be the best place to start.

            :param name:
            :return:
        """
        by_subject = self.__grades[name]
        score_sum, score_count = 0, 0
        for subject, scores in by_subject.items():
            subject_avg, total_weight = 0, 0
            for score, weight in scores:
                subject_avg += score * weight
                print('This is subject_avg:')
                print(subject_avg)
                total_weight += weight
                print('This is total_weight:')
                print(total_weight, end='\n\n')
            score_sum += subject_avg / total_weight
            print('This is score_sum:')
            print(score_sum, end='\n\n')
            score_count += 1
            print('This is score_count:')
            print(score_count, end='\n\n')
        return score_sum / score_count

book = WeightedGradebook()
book.add_student('Albert Einstein')
book.report_grade('Albert Einstein', 'Math', 80, .10)
book.report_grade('Albert Einstein', 'Math', 90, .40)
# book.report_grade('Albert Einstein', 'Math', 90, .10)

print("Total grade average: %d" % book.average_grade('Albert Einstein'))

