"""
    This module connects the abstract classes and the concrete implementations created
    by our MapReduce implementation. Those classes have reasonable interfaces and
    abstractions -- but that's only useful once the objects are constructed.

    This module builds the objects and orchestrates the MapReduce.
"""
import os
from threading import Thread

from classesandinheritance.constructgenericobjectswithatclassmethod.b_cncrt_mapreduce_implementation import \
    PathInputData, WorkersLineCountWorker


def generate_inputs(data_dir) -> 'Generator[PathInputData]':
    """
        This is a helper function that manually builds and connects the
        objects.

        It lists the contents of a directory and constructs a
        'PathInputData' instance for each file it contains.

        *** This is not a generic implementation ***

        :param data_dir:
        :return: PathInputData generator
    """
    print('Now in generate_inputs, making a generator!')
    for name in os.listdir(data_dir):
        yield PathInputData(os.path.join(data_dir, name), name)


def create_workers(input_lists) -> 'List[WorkersLineCountWorker]':
    """
        This function creates LineCounterWorker instances using the InputData
        instances returned by generate_inputs.

        *** This is not a generic implementation ***

        :param input_lists:
               An instance of InputData. The function generate_inputs is passed
               as an input to this field.
        :return: array of lineCounterWorkers
    """
    print('In create_workers with a generator (not sure how to prent without exhausting it yet)')
    print('In create_workers still. Just remembered for a method signature create_workers(input_lists)'
          , ', no generator exists until you actually call the generator for the first time.')
    workers = []
    for input_data in input_lists:
        workers.append(WorkersLineCountWorker(input_data))
    print('In create_workers created the generator by intereacting with input_lists like this:'
          , 'for input_data in input_lists: workers.append(LineCountWorker(input_data))'
          , 'this made a list of workers: \n\t'
          , workers)
    return workers


def execute(workers) -> 'result':
    """
        This function fans out the map function within the Worker class to
        multiple threads (this is because each worker utilizes I/O. Using
        threads allows another thread to run once the I/O is blocked.)

        The function then calls reduce repeatedly to combine the results
        into one final value.

        :param workers:
        :return:
    """
    print('\n\nIn execute(workers), just about to create a bunch of threads. Like this: '
          , 'threads = [Thread(target=w.map) for w in workers]')
    threads = [Thread(target=w.map) for w in workers]
    print('In execute(workers), Received a list of threads: ', threads, '\n')
    for thread in threads:
        print('In execute(workers), Now starting thread: ', thread)
        thread.start()
    for thread in threads:
        print('In execute(workers), Now joining thread: ', thread)
        thread.join()

    print('\n\nStill in execute(workers) completed all starting and joining of threads:')
    first, rest = workers[0], workers[1:]
    print('In execute(workers) right after first, rest = workers[0], workers[1:], \n\tFirst is: \n\t\t'
          , workers[0]
          , '\n\tand rest is:\n\t\t'
          , workers[1:]
          , '\n\n')
    for worker in rest:
        print('In execute(workers) for worker in rest: loop, \n\tFirst: \n\t\t'
              , first
              , '\n\tis calling reduce on itself for:\n\t\t', worker)
        first.reduce(worker)  # combining the reuslts into one final value
    return first.result


def mapreduce(data_dir):
    """
        This function connects all of the pieces execution functions (generate_inputs,
        create_workers, and execute) and the classes themselves (PathInputData, an
        instance of InputData, and LineCountWorker, an instance of Worker) to execute
        the MapReduce implementation.

        *** This is not a generic implementation ***

        :param data_dir:
               Takes a directory. It is assumed the directory has a list of files to
               be read, so lines can be counted.
        :return:
    """
    print("In mapreduce starting the process")
    inputs = generate_inputs(data_dir)  # returns a PathInputData generoator
    workers = create_workers(inputs)
    return execute(workers)


from tempfile import TemporaryDirectory
from os import listdir
from os.path import isfile, join
from shutil import copy


def write_test_file(tmpdir):
    print('This is the directory: ', tmpdir, end='\n\n')
    src = '/Users/syeedode/generic_projects/python_microservice/flakon/flakon'
    src_files = listdir(src)
    for file in src_files:
        fully_qualied = join(src, file)
        if(isfile(fully_qualied)):
            copy(fully_qualied, tmpdir)
            new_fully_qualified = join(tmpdir, file)
            if isfile(new_fully_qualified):
                linecount = 0
                print('\n\nUtlizing this file: ', new_fully_qualified)
                with open(new_fully_qualified) as items:
                    for lines in items:
                        print('This is line number', linecount, ":", lines,end='')
                        linecount += 1


with TemporaryDirectory() as tmpdirectory:
    write_test_file(tmpdirectory)
    print('\n\n\nNow for the action\n\n\n')
    result = mapreduce(tmpdirectory)

print('\n\nThere are', result, 'lines')


