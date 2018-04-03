
class InputData(object):
    """
        This is an abstract class for implementing a MapReduce Implementation.
        This class is a common class to represent the input data.
    """
    def read(self):
        raise NotImplementedError


class Worker(object):
    """
        This is an abstract class for implementing a MapReduce Implementation.
        This class consumes the input data in a standard way.
    """
    def __init__(self, input_data):
        self.input_data = input_data
        self.fileName = input_data.fileName
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self):
        raise NotImplementedError