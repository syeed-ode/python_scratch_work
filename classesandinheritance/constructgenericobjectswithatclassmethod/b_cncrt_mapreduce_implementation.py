from classesandinheritance.constructgenericobjectswithatclassmethod.a_abs_mapreduce_implementation import InputData, Worker


class PathInputData(InputData):
    """
        This is a concrete subclass of 'InputData' that reads data from a file on disk
    """
    def __init__(self, path, name):
        super().__init__()
        self.path = path
        self.fileName = name

    def read(self):
        return open(self.path).read()


class WorkersLineCountWorker(Worker):
    """
        This is a concrete subclass of 'Worker' that implemenets the specific
        MapReuce function: a simple newline counter.
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
