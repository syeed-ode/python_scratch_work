from classesandinheritance.constructgenericobjectswithatclassmethod.c_fnct_to_coordinate_non_polymphc_mapreduce import \
    execute, write_test_file
from classesandinheritance.constructgenericobjectswithatclassmethod.e_cncrt_mr_impl_with_generic_clsmethod import \
    LineCountWorkerWhichWasGenericized, PathInputDataGenericized


def mapreduce(worker_class, input_class, config):
    """
        This function now operates generically. Because of the genericity,
        the worker_class can now call generate_inputs directly (this occurs
        inside of the create_workers method), utilizing its own
        implementation of that method (a @classmethod)

        :param worker_class:

        :param input_class:
        :param config:
        :return:
    """
    workers = worker_class.create_workers(input_class, config)
    return execute(workers)


from tempfile import TemporaryDirectory


with TemporaryDirectory() as tmpdir:
    write_test_file(tmpdir)
    print('\n\n\nNow for the action\n\n\n')
    result = mapreduce(tmpdir, LineCountWorkerWhichWasGenericized, PathInputDataGenericized)

print('\n\nThere are', result, 'lines')
