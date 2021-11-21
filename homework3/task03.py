# I decided to write a code that generates data filtering
# object from a list of keyword parameters:


from functools import partial

from typing import Any


class Filter:
    """
    Helper filter class. Accepts a list of single-argument
    functions that return True if object in list conforms to some criteria
    """

    def __init__(self, functions):
        self.functions = functions

    def apply(self, data):
        return [item for item in data if all(i(item) for i in self.functions)]


"""
example of usage:
positive_even = Filter(lambda a: a % 2 == 0, lambda a: a > 0,
lambda a: isinstance(int, a)))
positive_even.apply(range(100)) should return only even numbers from 0 to 99
"""


def keyword_filter_func(key: Any, value: Any, value_check_sample: Any) -> bool:
    if key not in value_check_sample:
        return False
    return value == value_check_sample[key]


def make_filter(**keywords):
    """
    Generate filter object for specified keywords
    """
    filter_funcs = []
    for key, value in keywords.items():
        filter_funcs.append(partial(keyword_filter_func, key, value))
    return Filter(filter_funcs)


sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
]


# make_filter(name='polly', type='bird').apply(sample_data)
# should return only second entry from the list

# There are multiple bugs in this code. Find them all and
# write tests for faulty cases.
