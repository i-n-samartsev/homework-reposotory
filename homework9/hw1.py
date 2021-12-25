"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

>>> list(merge_sorted_files(['file1.txt', 'file2.txt']))
[1, 2, 3, 4, 5, 6]
"""
from heapq import merge
from pathlib import Path
from typing import Iterator, List, Union


class NotAnIntegerError(ValueError):
    """Exception class if file contains not only integers"""


def get_integers_from_file(filename: str) -> Iterator:
    with open(filename, mode='r') as file:
        for line_number, integer in enumerate(file, 1):
            try:
                yield int(integer.strip())
            except ValueError as err:
                raise NotAnIntegerError(f'{filename=} {line_number=} is not '
                                        f'an integer') from err


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:

    file_iterators = map(get_integers_from_file, file_list)
    yield from merge(*file_iterators)
