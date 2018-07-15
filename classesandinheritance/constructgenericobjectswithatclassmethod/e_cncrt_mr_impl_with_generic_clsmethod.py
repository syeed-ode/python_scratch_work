"""
    This module mirrors the b_cncrt_mapreduce_implementation module. Now it moves
    the generate_inputs function into a class method that was inherited from the
    superclass 'GenericInputData'.
"""
from classesandinheritance.constructgenericobjectswithatclassmethod.d_abs_mr_impl_with_generic_clsmethod import \
    GenericInputData, GenericWorker
import os


class PathInputDataGenericized(GenericInputData):
    """
        A concrete subclass of GenericInputData responsible for the implementation of
        the generate_inputs method.
    """

    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        return open(self.path).read()

    @classmethod
    def generate_inputs(cls, config):
        """
            A concrete implementation of GenericInputData's generate_inputs. It is
            direct contrast to the c_fnct_to_coordinate_non_polymphc_mapreduce
            module's generate_inputs.

            This @classmethod implementation allows our generate_inputs operation to
            be generic for any client.

            It is called by the d_abs_mr_impl_with_generic_clsmethod module's
            create_workers(), which is also an @classmethod.

            :param config:
                   A dictionary with a set of configuration parameters. It is used to
                   find the a directory with the input files.
            :return:
        """
        data_dir = config['data_dir']
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))


class LineCountWorkerWhichWasGenericized(GenericWorker):
    """
        This method has the same exact code as b_cncrt_mapreduce_implementation
        module's WorkersLineCountWorker. It's parent super class is different,
        however.

        The parent class utilizes class polymorphism: the @classmethod to
        genericize the creation of generic workers.
    """
    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')
        print('\tPart of a thread\n\t\tIn LineCountWorker.map Read data for file: '
              , self.fileName
              , 'with a file count of:'
              , self.result
              , end='\n')

    def reduce(self, other):
        print('In LineCountWorker.reduce(self, other) where first:'
              , self.fileName, 'with a size of', self.result
              , 'is reducing file data for file:'
              , other.fileName, 'with a size of', other.result)
        self.result += other.result
