from collections import defaultdict

def log_missing():
    """
        This function demonstrates how to provide stateless "hooks". (The "hook"
        is used by an external client (outside the function).

        This "hook" function is passed into the defaultdict built-in function.
        defaultdict calls the hook. Then the hook logs each time a key is
        misssing and returns 0. It will be called each time by defaultdict
        data structure when it doesn't have a key.
    """
    print('Key added')
    return 0

'''
    Given an initial dictionary and a set of desired increments, we can cause
    the 'log_missing' function to run and print twice (for 'red' and 'orange').
    This is because of collections defaultdict takes a 'default_factory' 
    hook. 
    
    The ending dictionary has the missing elements added as a result of being a 
    defualtdict.
'''
current = {'green': 12, 'blue': 3}
increments = [('red', 5), ('blue', 17), ('orange', 9)]

result = defaultdict(log_missing, current)
print('Before:', dict(result))

for key, amount in increments:
    result[key] += amount

print('After:', dict(result))


def increment_with_report(current=None, increments=None):
    """
        This function demonstrates how to provide hooks with state.
        It uses a closure maintain the state. The hook is called
        within this enclosing function.

        This method utilizes a closure hook that counts the number
         of items that were missing from an initial dictionary.

        :param current:
        :param increments:
        :return:
    """
    added_count = 0

    def missing():
        """
            This function is a hook into defaultdict it is utilized
            by the enclosing function.

            Utilizing hooks separate side effects from deterministic
            behavior.

            #
            # The purpose of the closure is to provide state
            # (functions don't have this ability)
            #
            :return:
        """
        nonlocal added_count  # Stateful closure
        added_count += 1
        return 0

    result = defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount

    return result, added_count

current = {'green': 12, 'blue': 3}
increments = [('red', 5), ('blue', 17), ('orange', 9)]

result, count = increment_with_report(current, increments)
assert count == 2


class CountMissing(object):
    """
        This class provides state in lui of utilizing a stateless
        method and a closure. There are two benefits:
            1) it improves readability and
            2) you clients are free to use the class at will
               (instead of having the function be the client of the
               closure).
    """
    def __init__(self):
        self.added = 0

    def missing(self):
        self.added += 1
        return 0

current = {'green': 12, 'blue': 3}
increments = [('red', 5), ('blue', 17), ('orange', 9)]

counter = CountMissing()
result = defaultdict(counter.missing, current)  # Method reference

for key, amount in increments:
    result[key] += amount

assert counter.added == 2


class BetterCountMissing(object):
    """
        This class highlights the deficiencies in CountMissing. In
        CountMissing readability suffers. How and when to use the
        missing method is not clear.

        Using dunder call allows this class to be called like a
        method. It also retuns true when called by the 'callable'
        built-in function.
    """
    def __init__(self):
        self.added = 0

    def __call__(self, *args, **kwargs):
        """
            The method indicates to clients that the intended use
            for this class is to be used where a function call would
            be used.

            By using a class the directive to any client is that
            state is maintained.

            :param args:
            :param kwargs:
            :return:
        """
        self.added += 1
        return 0

counter = BetterCountMissing()
print('This is counter: ', counter())
counter.added -= 1
assert callable(counter)

current = {'green': 12, 'blue': 3}
increments = [('red', 5), ('blue', 17), ('orange', 9)]

result = defaultdict(counter, current)  # The counter hook relies on __call__
for key, amount in increments:
    result[key] += amount
print("This is the current state of the counter: ", counter.added)
assert counter.added == 2
