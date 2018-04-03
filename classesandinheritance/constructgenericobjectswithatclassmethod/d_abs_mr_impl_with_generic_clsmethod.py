"""
    This module mirrors the a_abs_mapreduce_implementation module.  There is
    one key difference:

        the classes in this module implement class operations generically.

"""


class GenericInputData(object):
    """
        This class extends the 'InputData' class by adding a class method that's
        responsible for creating new InputData instances. The class now has a
        common interface.
    """
    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError


class GenericWorker(object):
    def __init__(self, input_data):
        self.input_data = input_data
        self.fileName = input_data.fileName
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self):
        raise NotImplementedError

    @classmethod
    def create_workers(cls, input_class, config):
        """
            This method replaces c_fnct_to_coordinate_non_polymphc_mapreduce
            module's create_workers. That modules create_workers was dependent
            upon WorkersLineCountWorker. This create_workers is completely
            generic. It uses cls to construct instances instead of
            WorkersLineCountWorker's __init__ method.

            This method takes a generic 'input_class' which demonstrates the
            ability to utilize polymorphism even though Python doesn't support
            constructor polymorphism.

            input_class.generate_inputs shows how to utilize class polymorphism.

            cls provids an alternate way to construct 'GenericWorker' objects
            besides using the __init__ method directly. cls constructs concrete
            subclass instances of the GenericWorker class.

            cls is used as a generic constructor.


            :param input_class:
                   Instance of 'GenericInputData' where the method being
                   referenced on the class is an @classmethod.
            :param config:
            :return:
        """
        workers = []
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers
